import os
import tempfile
import base64
import re
from docxtpl import DocxTemplate, RichText
from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.forms.models import model_to_dict
from weasyprint import HTML, CSS


def add_css(output_text, css_file_name):
    css_to_add_url = find('css/{css_file_name}.css'.format(css_file_name=css_file_name))
    css_out = '<style>{css}</style>'.format(
        css=open(css_to_add_url).read())
    output_text += css_out
    return output_text


def convert_html_to_pdf(sourceHtml, style_sheet_name):
    temp_file_out = tempfile.NamedTemporaryFile(suffix='pdf')
    try:

        HTML(string=sourceHtml).write_pdf(
            temp_file_out.name,
            stylesheets=[CSS(filename=find('css/{style_sheet_name}'.format(style_sheet_name=style_sheet_name)))]
        )
        result = temp_file_out.read()
    except Exception as e:
        return e
    return result


def replace_html_media_images_with_base64(html_in):
    try:
        image_regex = r'<img(.*)>'
        groups = [x.group() for x in re.finditer(image_regex, html_in)]
        for group in groups:
            image_tag = str(group)
            image_path = re.search(r'src=\"(.*?)\"', image_tag).group(1)
            image_location = settings.MEDIA_ROOT.replace('/media', '') + image_path.replace('uploads', 'project_image')
            width = re.search(r'width="(.*)"', image_tag).string
            height = re.search(r'height="(.*)"', image_tag).string
            with open(image_location, "rb") as img_file:
                base64code = base64.b64encode(img_file.read())
            image_result = ('<img src="data:image/png;base64, {base64code}"/>').format(base64code=base64code)
            html_in = re.sub(group, image_result, html_in)
        return html_in
    except Exception as e:
        return e


def replace_html_relative_images_with_base64(html_in, template_location):
    try:
        image_regex = r'<img(.*)>'
        groups = []
        for x in re.finditer(image_regex, html_in):
            if not x:
                continue
            try:
                groups.append(x.group())
            except AttributeError:
                continue
        for group in groups:
            image_tag = str(group)
            image_exp = re.compile('src=\"(.*?)\"')
            # image_extension_exp = r'\.([0-9a-z]+$)'
            image_path = re.search(r'src=\"(.*?)\"', image_tag).group(1)
            if image_path.find('home') > 0:
                image_location = image_path
            else:
                image_location = template_location + image_path
                if not os.path.exists(image_location):
                    image_location = os.path.join(
                        settings.MEDIA_ROOT,
                        image_path
                    )
                if not os.path.exists(image_location):
                    continue
            try:
                width = re.search(r'width=\"(.*)\"', image_tag).group(1)
            except AttributeError:
                width = 0
            try:
                height = re.search(r'height=\"(.*)\"', image_tag).group(1)
            except AttributeError:
                height = 0
            try:
                css_class = re.search(r'class=\"(.*?)\"', image_tag).group(1)
            except AttributeError:
                try:
                    css_class = re.search(r"class=\'(.*)\'", image_tag).group(1)
                except AttributeError:
                    css_class = ''
            image_extension = re.search("\.([0-9a-z]+)", image_tag).group(1)
            if image_extension == 'svg':
                image_extension = 'svg+xml'
            image_test_substring = 'data:image/{image_extension};base64'.format(image_extension=image_extension)
            if image_location.find(image_test_substring) > 0:  # Assumes this is already base64
                base64code = image_location
            else:
                with open(image_location, "rb") as img_file:
                    base64code = base64.b64encode(img_file.read())
            image_result = (
                '<img class="{css_class}" src="data:image/{image_extension};base64, {base64code}"/>').format(
                css_class=css_class,
                image_extension=image_extension,
                base64code=base64code,
                )
            html_in = re.sub(group, image_result, html_in)
        return html_in
    except Exception as e:
        return html_in


def strip_rt_tags(text_in):
    text_in = (
        text_in.
        replace('<p>', '').
        replace('<br/>', '').
        replace('<br>', '').
        replace('</p>', '').
        replace('&nbsp;', ' ').
        replace('<span>', '').
        replace('</span>', ''))
    return text_in


def get_richtext_and_images(text_source):
    text_in = text_source
    images = {}
    image_count = 0
    image_location = text_in.find('<img')
    while image_location >= 0:
        image_count += 1
        text_in = text_in[image_location - 1:]
        next_image_tag = text_in[0:text_in.find('>')] + '>'
        try:
            src = re.search(r'src=\"(.*?)\"', next_image_tag).group(1)
            x_size = re.search(r'width=\"(.*?)\"', next_image_tag).group(1)
            y_size = re.search(r'height=\"(.*?)\"', next_image_tag).group(1)
        except AttributeError:
            src = ''
            x_size = 0
            y_size = 0
        text_in = text_in[text_in.find('/>'):]
        image_location = text_in.find('<img')
        image_number = 'myimage{number}'.format(number=image_count)
        text_source = text_source.replace(next_image_tag, ' {{ ' + image_number + ' }}')
        images[image_number] = {}
        images[image_number]['src'] = src
        images[image_number]['x_size'] = float(x_size) * 100
        images[image_number]['y_size'] = float(y_size) * 100
    return text_source, images


# ToDo: Add and link docx images
def generate_docx(request, project, layout):
    try:
        template_path = find('layouts/{layout}.docx'.format(layout=layout))

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
        return new_zipfile_path
    except Exception as exception:
        i = exception