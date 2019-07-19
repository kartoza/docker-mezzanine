import tempfile
from datetime import datetime


from django.db import models
from django.template.loader import render_to_string
from kartoza_project.models.project_image import ProjectImage
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Slugged, Orderable
from mezzanine.utils.models import AdminThumbMixin


class Project(Orderable, Slugged, AdminThumbMixin):
    short_description = models.CharField(
        null=True,
        blank=True,
        verbose_name='Project short description',
        max_length=1000,
    )

    project_details = RichTextField(
        null=True,
        blank=True,
        verbose_name='Project details'
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

    value = models.DecimalField(
        verbose_name='Project value',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    consultants = models.ManyToManyField(

        'kartoza_project.Reference',
        related_name='consultants',
        null=True,
        blank=True,
    )

    staff_involved = models.ManyToManyField(
        'kartoza_project.Reference',
        related_name='staff_involved',
        null=True,
        blank=True,
    )

    description = RichTextField(
        "description",
        help_text=(
            "This field can contain HTML and should contain a "
            "few paragraphs describing the background of "
            "the project."),
        default="",
        blank=True)

    services_provided = RichTextField(
        "services_provided",
        help_text=(
            "This field can contain HTML and should contain a "
            "few paragraphs describing the background of "
            "the project."),
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
            "A link to the project's github page."),
        max_length=255)

    admin_thumb_field = 'thumbnail'

    def __unicode__(self):
        return self.title

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
            starting_template = render_to_string(
                'world_bank_format.md', {'project': self,
                                         'consultants': self.consultants.all(),
                                         'staff': self.staff_involved.all(),
                                         'clients': self.clients.all()})

            return starting_template
