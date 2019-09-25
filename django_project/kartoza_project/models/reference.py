from django.db import models


class Reference(models.Model):
    person = models.ForeignKey(
        'kartoza_project.Person',
        null=True,
        related_name='reference_person'
    )

    project = models.ForeignKey(
        'kartoza_project.Project',
        null=True,
        related_name='project_references'
    )

    role = models.ForeignKey(
        'kartoza_project.Role',
        null=True,
        related_name='reference_role'
    )

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        try:
            return self.person.name
        except AttributeError:
            return ""