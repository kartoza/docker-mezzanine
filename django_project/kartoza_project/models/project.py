import tempfile
import base64
import re
from datetime import datetime
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from kartoza_project.models.project_image import ProjectImage
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Slugged, Orderable
from mezzanine.utils.models import AdminThumbMixin


class Project(Orderable, Slugged, AdminThumbMixin):

    images_dict = {}
    short_description = models.CharField(
        null=True,
        blank=True,
        verbose_name='Project short description',
        max_length=1000,
    )

    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='project',
        verbose_name='Project thumbnail'
    )

    country = models.CharField(
        null=True,
        blank=True,
        help_text=(
            "In which country was the project located"),
        max_length=255
    )

    location = models.CharField(
        null=True,
        blank=True,
        help_text=(
            "Where was the project located more specifically"),
        max_length=255
    )

    categories = models.ManyToManyField(
        'kartoza_project.ProjectCategory',
        verbose_name='Categories',
        null=True,
        blank=True,
        related_name='project_category'
    )

    date_start = models.DateField(
        null=True,
        blank=True
    )

    date_end = models.DateField(
        null=True,
        blank=True
    )

    clients = models.ManyToManyField(
        'clients.Client',
        null=True,
        blank=True,
        related_name="clients"
    )

    contact_person = models.ForeignKey(
        'kartoza_project.Reference',
        null=True,
        on_delete=models.PROTECT,
        related_name='contact_person')

    consultants = models.ManyToManyField(
        'kartoza_project.Reference',
        related_name='consultants',
        null=True,
        blank=True,
        help_text='External company/individuals contracted to assist with the work done.'
    )

    staff_involved = models.ManyToManyField(
        'kartoza_project.Reference',
        related_name='staff_involved',
        null=True,
        blank=True,
        help_text='All kartoza staff who worked on this project.',
    )

    description = RichTextField(
        "description",
        help_text=(
            "This field can contain HTML and should contain a "
            "few paragraphs describing the background of "
            "the project. As used in the world bank template."),
        default="",
        blank=True)

    services_provided = RichTextField(
        "services_provided",
        help_text=(
            "This field can contain HTML and should contain a "
            "few paragraphs describing the background of "
            "the project. As used in the world bank template."),
        default="",
        blank=True)

    approximate_contract_value = models.IntegerField(
        blank=True,
        null=True,
        help_text="Approximate value of the contract (US $)")

    duration_of_assignment = models.IntegerField(
        blank=True,
        null=True,
        help_text="Duration of the assignment (months).")

    total_staff_months = models.IntegerField(
        blank=True,
        null=True,
        help_text="Total number of staff-months required to complete the "
                  "project.")

    total_staff_months_by_kartoza = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of professional staff-months provided by Kartoza.")

    published = models.BooleanField(
        'Published to public gallery',
        default=False)

    technologies = models.CharField(
        null=True,
        blank=True,
        help_text=(
            "Comma seperated list of technologies associated with the project"),
        max_length=1000
    )

    tags = models.CharField(
        null=True,
        blank=True,
        help_text=(
            "Comma seperated list of keywords associated with the project"),
        max_length=1000
    )

    public_page = models.URLField(
        null=True,
        blank=True,
        help_text=(
            "If available to the public, where can the project be found?"),
        max_length=255)
    github_page = models.URLField(
        null=True,
        blank=True,
        help_text=(
            "A link to the project's g  ithub page."),
        max_length=255)

    admin_thumb_field = 'thumbnail'

    contact_person = models.ForeignKey(
        'kartoza_project.Reference',
        null=True,
        on_delete=models.PROTECT,
        related_name='contact_person')

    def __unicode__(self):
        return unicode(self.title)

    @property
    def sorted_clients_set(self):
        return self.clients.order_by('title')

    @property
    def ongoing(self):
        if not self.date_start and not self.date_end:
            return False
        if not self.date_end and self.date_start:
            return True
        if self.date_start >= datetime.now().date():
            return False
        if self.date_end >= datetime.now().date():
            return True

    @property
    def image_urls(self):
        image_urls = []
        images = ProjectImage.objects.filter(project__id=self.id).all()
        for image in images:
            image_urls.append(image.image.url)
        return image_urls

    @property
    def tags_list(self):
        return set(map(unicode.strip, self.tags.split(',')))

    @property
    def technologies_list(self):
        return set(map(unicode.strip, self.technologies.split(',')))

    @property
    def search_string(self):
        return '{title} {description} {services_provided} {brief}'.format(
            title=self.title,
            description=self.description,
            services_provided=self.services_provided,
            brief=self.short_description
        )

    def get_template(self, template):
        if template == 'world_bank_format':
            template_name = 'world_bank_format.md'
        elif template == 'public_portfolio':
            template_name = 'public_portfolio.html'
        starting_template = render_to_string(
            template_name, {'project': self,
                                     'consultants': self.consultants.all(),
                                     'staff': self.staff_involved.all(),
                                     'clients': self.clients.all()})
        return starting_template

    @property
    def duration(self):
        if not self.date_end:
            return 'Ongoing'
        return ((self.date_end.year - self.date_start.year) * 12 +
                self.date_end.month - self.date_end.month)
    #
    @property
    def export_description(self):
        safe_description = self.description
        safe_description = (
            safe_description.
                replace('<p>', '').
                replace('<br/>', '').
                replace('<br>', '').
                replace('</p>', '').
                replace('&nbsp;', ' '))
        text, images = get_richtext_and_images(safe_description)
        for image_key in images.keys():
            self.images_dict[image_key] = images[image_key]
        return text, images

    @property
    def export_html_description(self):
        safe_description = self.description
        safe_description = (
            safe_description.
                replace('<p>', '').
                replace('</p>', '<br/>'))
        safe_description = replace_html_images_with_base64(safe_description)
        return safe_description or u'None'

    @property
    def export_services_provided(self):
        safe_services = self.services_provided
        safe_services = (
            safe_services.
            replace('<p>', '').
            replace('<br/>', '').
            replace('<br>', '').
            replace('</p>', '').
            replace('&nbsp;', ' '))
        text, images = get_richtext_and_images(safe_services)
        for image_key in images.keys():
            self.images_dict[image_key] = images[image_key]
        return text, images

    @property
    def export_html_services_provided(self):
        safe_services = self.services_provided
        safe_services = (
            safe_services.
                replace('<p>', '').
                replace('</p>', '<br/>'))
        return safe_services or u'None'

    def strip_rt_tags(self, text_in):
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

    def images(self):
        return self.images_dict or u'None'


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def get_richtext_and_images(text_source):
    text_in = text_source
    # image_locations = [m.start() for m in re.finditer(text_in, '<img')]
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
            src  = ''
            x_size = 0
            y_size = 0

        text_in = text_in[text_in.find('/>'):]
        image_location = text_in.find('<img')
        # image_number = 'myimage{number}'.format(number=image_count)
        # text_source = text_source.replace(next_image_tag, ' {{ ' + image_number + ' }}')
        # images[image_number] = {}
        # images[image_number]['src']= src
        # images[image_number]['x_size']= float(x_size) * 100
        # images[image_number]['y_size'] = float(y_size) * 100

    return text_source, images


def replace_html_images_with_base64(html_in):
    try:
        image_regex = r'<img(.*)>'
        groups = [x.group() for x in re.finditer(image_regex, html_in)]
        for group in groups:
            image_tag = str(group)
            image_exp = re.compile('src=\"(.*?)\"')
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