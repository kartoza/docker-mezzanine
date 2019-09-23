from django.db import models


class Reference(models.Model):
    person = models.ForeignKey(
        'kartoza_project.Role',
        null=True,
        related_name='project_references'
    )

    project = models.ForeignKey(
        'kartoza_project.Project',
        null=True,
        related_name='project_references'
    )

    role = models.ForeignKey(
        'kartoza_project.Role',
        null=True,
        related_name='project_references'
    )

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        return self.person.name

    @property
    def role(self):
        return self.role.name