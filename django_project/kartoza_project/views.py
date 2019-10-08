import tempfile
from datetime import datetime
from wsgiref.util import FileWrapper
from weasyprint import HTML, CSS
import pypandoc
from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render as django_render
from mezzanine.conf import settings
from mezzanine.utils.views import render, paginate
from .models import Project, ProjectCategory, ProjectImage, Reference


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
        project_images = Project.objects.filter(published=True).values(
            'id', 'project_images__image').all()
        projects = Project.objects.filter(
            published=True).all()
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
            try:
                if conversion_format == 'pdf':
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
                    output_text = convertHtmlToPdf(output_text)
                response = HttpResponse(output_text)
                return response
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse()


def add_css(output_text):
    css_to_add_url = find('css/pandoc.css')
    css_out = '<style>{css}</style>'.format(
        css=open(css_to_add_url).read())
    output_text += css_out
    return output_text


def convertHtmlToPdf(sourceHtml):
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
             'images': images }
        )


def get_reference(request):
    if request.method == 'POST':
        reference = ''
        reference_id = request.POST['reference_id']
        if len(reference_id) > 0:
            reference = Reference.objects.filter(pk=int(reference_id))
            reference_json = serializers.serialize('json', reference)
        return HttpResponse(reference_json)
