from datetime import datetime

from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Slugged, Orderable
from mezzanine.utils.models import AdminThumbMixin


class Project(Orderable, Slugged, AdminThumbMixin):


    short_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Project short description'
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
        Person,
        through='Reference',
        related_name='consultants')
    staff_involved = models.ManyToManyField(
        Person,
        through='Reference',
        related_name='staff_involved')

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
