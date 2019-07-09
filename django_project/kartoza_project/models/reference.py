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
        related_name='project_references'
    )

    def __unicode__(self):
        return self.name
