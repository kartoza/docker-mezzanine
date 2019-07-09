from django.db import models
from mezzanine.utils.models import AdminThumbMixin


class ProjectImage(AdminThumbMixin, models.Model):
    image = models.ImageField()

    caption = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )

    project = models.ForeignKey(
        'kartoza_project.Project',
        related_name='project_images',
    )

    admin_thumb_field = 'image'
