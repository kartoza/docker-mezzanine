import tempfile
import zipfile
import os
from django.utils.encoding import smart_str, smart_unicode
import re
from datetime import datetime
from wsgiref.util import FileWrapper
from weasyprint import HTML, CSS
from docx import *
import pypandoc
from docxtpl import DocxTemplate, RichText, InlineImage
from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render as django_render

from django.template import Template, engines
from django.forms.models import model_to_dict
from mezzanine.conf import settings
from mezzanine.utils.views import render, paginate
from .models import Project, ProjectCategory, ProjectImage, Reference
from updateable_zipfile import UpdateableZipFile
import shutil




def project_list(request, category=None,
                 template='kartoza_project/project_list.html'):
    """
    Display a list of project that are filtered by category.
    Custom templates are checked for using the name
    ``people/person_list_XXX.html`` where ``XXX`` is the category's slug.
    """
    settings.use_editable()
    templates = []
    projects = Project.objects.all()
    if category is not None:
        category = get_object_or_404(ProjectCategory, slug=category)
        projects = projects.filter(categories=category)
        templates.append(u'kartoza_project/project_list_%s.html' %
                         unicode(category.slug))

    # requires Django VERSION >= (1, 4):
    projects = projects.prefetch_related('categories')

    projects = paginate(projects, request.GET.get('page', 1),
                        settings.PROJECTS_PER_PAGE,
                        settings.MAX_PAGING_LINKS)
    context = {'projects': projects, 'category': category}
    templates.append(template)
    return render(request, templates, context)


def project_detail(request, slug,
                   template='kartoza_project/project_detail.html'):
    """
    Custom templates are checked for using the name
    ``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
    person's slug.
    """
    project = get_object_or_404(Project, slug=slug)
    images = ProjectImage.objects.filter(project=project).order_by('id')
    references = Reference.objects.filter(project=project).order_by('name')

    context = {
        'project': project,
        'images': images,
        'references': references
    }
    templates = [u'kartoza_project/project_detail_%s.html' % unicode(slug),
                 template]
    return render(request, templates, context)


def project_list_ongoing(request, template='kartoza_project/project_list.html'):
    templates = []
    projects = Project.objects.all().exclude(
        date_start__isnull=True,
        date_end__isnull=True
    )
    projects = projects.filter(
        Q(date_end__isnull=False, date_end__gt=datetime.now().date()) |
        Q(date_end__isnull=True, date_start__isnull=False)
    )
    # requires Django VERSION >= (1, 4):
    projects = projects.prefetch_related('categories')

    projects = paginate(projects, request.GET.get('page', 1),
                        settings.PROJECTS_PER_PAGE,
                        settings.MAX_PAGING_LINKS)
    context = {'projects': projects}
    templates.append(template)
    return render(request, templates, context)


def project_gallery(request):
    if request.method == 'GET':
        project_images = Project.objects.values(
            'id', 'project_images__image').all()
        projects = Project.objects.all()
        for project in projects:
            if not project.thumbnail:
                project.thumbnail = {'url':''}
        tag_list = ''
        technology_list = ''
        for project in projects:
            tag_list += project.tags + ','
            technology_list += project.technologies + ','
        try:
            tags = set(map(unicode.strip, tag_list.split(',')))
            tags.remove('')
        except TypeError:
            tags = ()
        try:
            technologies = set(map(unicode.strip, technology_list.split(',')))
            technologies.remove('')
        except TypeError:
            technologies = ()

        return django_render(
            request,
            'export_list.html',
            {'projects': projects,
             'tags': tags,
             'technologies': technologies,
             'project_images': project_images}
        )


def export_project(request, project_id, type):
    if request.method == 'GET':
        project = Project.objects.get(id=project_id)
        response = HttpResponse(
            FileWrapper(project.get_template('basic', str(type).lower())),
            content_type='text/html')
        response['Content-Disposition'] = (
            'attachment; filename=output.{extension}'.format(extension=type))
        return response


def export_projects(request):
    if request.method == 'POST':
        projects_to_export = (
            str(request.POST['projects_to_export']).split(',')[0::2])
        format = request.POST['format']
        layout = request.POST['layout']
        response_string = ''

        if len(projects_to_export) > 0:
            for key in projects_to_export:
                next_project = Project.objects.get(pk=key)
                next_file_text = (
                    next_project.get_template(layout))
                response_string += next_file_text
            tmpFileOut = tempfile.NamedTemporaryFile()
            conversion_format = format
            if conversion_format == 'pdf':
                try:
                    conversion_format = 'html'
                    output = pypandoc.convert_text(
                        response_string,
                        to=conversion_format,
                        format='md',
                        outputfile=tmpFileOut.name)
                    output_text = tmpFileOut.read()

                    if conversion_format == 'html':
                        output_text = add_css(output_text)
                    if format == 'pdf':
                        output_text = convert_html_to_pdf(output_text)
                    response = HttpResponse(output_text)
                    return response
                except Exception as e:
                    return HttpResponse(e)
            if conversion_format == u'odt':
                try:
                    conversion_format = 'html'
                    output = pypandoc.convert_text(
                        response_string,
                        to=conversion_format,
                        format='md',
                        outputfile=tmpFileOut.name)
                    output_text = tmpFileOut.read()
                    tmpFileOut2 = tempfile.NamedTemporaryFile()
                    # output_text = add_css(output_text)
                    output = pypandoc.convert_text(output_text, 'odt', format='html', outputfile=tmpFileOut2.name)
                    output_text = tmpFileOut2.read()
                    response = HttpResponse(output_text)
                    return response
                except Exception as e:
                    return HttpResponse(e)
            if conversion_format == u'html':
                try:
                    conversion_format = 'html'
                    output = pypandoc.convert_text(
                        response_string,
                        to=conversion_format,
                        format='md',
                        outputfile=tmpFileOut.name)
                    output_text = tmpFileOut.read()
                    output_text = add_css(output_text)
                    response = HttpResponse(output_text)
                    return response
                except Exception as e:
                    return HttpResponse(e)
            if conversion_format == u'docx':

                # generated_docx = find('layouts/test2.docx')
                # try:
                #     conversion_format = 'html'
                #     # output = pypandoc.convert_file(
                #     #     generated_docx,
                #     #     to=conversion_format,
                #     #     format='docx',
                #     #     outputfile=tmpFileOut.name)
                #     output_text = convert_to_html(generated_docx)
                #
                #     # # output_text = add_css(output_text)
                #     response = HttpResponse(output_text)
                #
                #     return response
                # except Exception as e:
                #     return HttpResponse(e)
                generated_docx = generate_docx(request, 2)
                zip_file = open(generated_docx, 'r')
                response = HttpResponse(zip_file, content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename="%s"' % 'result.docx'
                return response
        else:
            return HttpResponse()


def add_css(output_text):
    css_to_add_url = find('css/pandoc.css')
    css_out = '<style>{css}</style>'.format(
        css=open(css_to_add_url).read())
    output_text += css_out
    return output_text


def convert_html_to_pdf(sourceHtml):
    temp_file_in = tempfile.NamedTemporaryFile()
    temp_file_out = tempfile.NamedTemporaryFile(suffix='pdf')
    temp_file_in.write(sourceHtml)
    try:
        HTML(temp_file_in.name).write_pdf(
            temp_file_out.name,
            stylesheets=[CSS(filename=find('css/pandoc.css'))])
        result = temp_file_out.read()
    except Exception as e:
        return e
    return result


def view_project(request, project_id):
    if request.method == 'GET':
        project = Project.objects.filter(pk=project_id).first()
        images = ProjectImage.objects.filter(
                 project__id=project.id).all()
        clients = project.clients.values('name', 'title', 'logo').all()
        # form = ProjectForm(project
        return django_render(
            request,
            'view_project.html',
            {'project': project,
             'consultants': project.consultants.all(),
             'staff_involved': project.staff_involved.all(),
             'clients': clients,
             'images': images}
        )


def view_project_details(request, project_id):
    if request.method == 'GET':
        project = Project.objects.filter(pk=project_id).first()
        images = ProjectImage.objects.filter(
                 project__id=project.id).all()
        clients = project.clients.values('name', 'title', 'logo').all()
        # form = ProjectForm(project
        return django_render(
            request,
            'view_project_details.html',
            {'project': project,
             'consultants': project.consultants.all(),
             'staff_involved': project.staff_involved.all(),
             'clients': clients,
             'images': images}
        )


def get_reference(request):
    if request.method == 'POST':
        reference = ''
        reference_id = request.POST['reference_id']
        if len(reference_id) > 0:
            reference = Reference.objects.filter(pk=int(reference_id))
            reference_json = serializers.serialize('json', reference)
        return HttpResponse(reference_json)


def generate_docx(request, project_id):
    try:
        template_path = find('layouts/template.docx')
        project = Project.objects.filter(pk=project_id).first()
        temp_directory = tempfile.mkdtemp()
        temp_directory_store = tempfile.mkdtemp()


        new_zipfile_path = temp_directory_store+'/zip_result.docx'

        doc = DocxTemplate(template_path)
        context = {}

        context['project'] = model_to_dict(project)

        drt = RichText()
        drt_text, drt_images = project.export_description
        drt.add(drt_text, style='Text Body')
        context['project']['drt'] = drt
        srt = RichText()
        srt_text, srt_images = project.export_services_provided
        srt.add(srt_text, style='Text Body')
        context['project']['drt'] = srt


        doc.render(context)
        doc.save(new_zipfile_path)

        # regex1 = re.compile(r"^(.*?(\bproject_title\b)[^$]*)$")
        # replace1 = r"your replace string"
        # filename = template_path
        # doc = Document(filename)
        # docx_replace_regex(doc, regex1, replace1)
        # doc.save(temp_directory_store+'/zip_result.docx')


            # parsed_content_value = re.findall('<w:body>(.*)</w:body>', content_value)[0]
            # template = django_engine.from_string(parsed_content_value)
            # result = template.render(context)
            # with open(content_path, 'w+') as f:
            #     try:
            #
            #         f.write(smart_str(result))
            #     except Exception as exception:
            #         i = exception
            #     i =0

        # with zipfile.ZipFile(new_zipfile_path, 'w') as zip_ref:
        # zip_folder(temp_directory, new_zipfile_path)
        # src = new_zipfile_path + '.zip'
        # dst = new_zipfile_path + '.docx'
        # os.rename(src, dst)
        return new_zipfile_path

    except Exception as exception:
        i = exception


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths


def zip_folder(directory, zip_file_name):
    shutil.make_archive(zip_file_name, 'zip', directory)


def print_path(path):
    print(os.listdir(path))
    folders = []
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))

    for f in folders:
        print(f)


def docx_replace_regex(doc_obj, regex , replace):
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex , replace)


def docx_replace_images(file_path, project):
    temp_directory = tempfile.mkdtemp()
    inline_template = find('layouts/docx_inline_image.xml')

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_directory)
        temp_directory = tempfile.mkdtemp()
        content_path = '{temp_dir}/word/document.xml'.format(temp_dir=temp_directory)
        print_path(temp_directory)
        with open(content_path, 'r') as content_file:
            content_value = content_file.read()

        context = model_to_dict(project.images)
        django_engine = engines['django']


def generate_inline_image_tag(template_path, image_dict):
    with open(template_path, 'r') as content_file:
        content_value = content_file.read()
