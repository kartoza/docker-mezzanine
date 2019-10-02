import tempfile
import zipfile
import os
import shutil
from docxtpl import DocxTemplate, RichText, InlineImage
from django.contrib.staticfiles.finders import find
from django.template import engines
from django.forms.models import model_to_dict
from .models import Project



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


def add_css(output_text):
    css_to_add_url = find('css/pandoc.css')
    css_out = '<style>{css}</style>'.format(
        css=open(css_to_add_url).read())
    output_text += css_out
    return output_text


def convert_html_to_pdf(sourceHtml):
    temp_file_in = tempfile.NamedTemporaryFile()
    temp_file_out = tempfile.NamedTemporaryFile(suffix='pdf')
    # temp_file_in.write(sourceHtml)
    try:

        HTML(string=sourceHtml).write_pdf(
            temp_file_out.name,
            stylesheets=[CSS(filename=find('css/public_portfolio.css'))]
        )
        result = temp_file_out.read()
    except Exception as e:
        return e
    return result
