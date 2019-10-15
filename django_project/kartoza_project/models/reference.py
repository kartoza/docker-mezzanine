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

    role_relation = models.ForeignKey(
        'kartoza_project.Role',
        null=True,
        related_name='reference_role'
    )

    @property
    def contact_detail(self):
        if len(self.email) > 0:
            return str(self.email)
        elif len(self.telephone) > 0:
            return str(self.telephone)
        else:
            return "Unavailable"

    def __unicode__(self):
        try:
            return self.person.name
        except:
            return ""

    @property
    def name(self):
        try:
            return self.person.name
        except:
            return ""

    @property
    def url(self):
        try:
            return self.person.url
        except:
            return ""

    @property
    def description(self):
        try:
            return self.role_relation.description
        except:
            return ""

    @property
    def telephone(self):
        try:
            return self.person.telephone
        except:
            return ""

    @property
    def email(self):
        try:
            return self.person.email
        except:
            return ""
