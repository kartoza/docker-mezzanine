from django.db import models


class Reference(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    url = models.URLField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    project = models.ForeignKey(
        'kartoza_project.Project',
        null=True,
        related_name='project_references'
    )

    telephone = models.CharField(
        blank=True,
        help_text='Telephone number',
        max_length=16)

    email = models.EmailField(
        null=True,
        blank=True,
        help_text='A contact email address for the reference',
        verbose_name='Email')

    role = models.CharField(
        blank=True,
        help_text='Role in the project',
        max_length=255)

    def __unicode__(self):
        return self.name
