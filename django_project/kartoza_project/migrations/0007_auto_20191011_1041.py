# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def create_reference(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.

    Person = apps.get_model('kartoza_project', 'Person')
    Role = apps.get_model('kartoza_project', 'Role')
    Reference = apps.get_model('kartoza_project', 'Reference')

    for reference in Reference.objects.all():
        try:
            existing_role = Role.objects.get(name=reference.old_role)
            reference.role = existing_role
        except:
            role = Role()
            role.name = reference.old_role
            role.description = ''
            role.save()
            reference.role = role
        try:
            existing_person = Person.objects.get(name=reference.name)
            reference.person = existing_person
        except:
            person = Person()
            person.name = reference.name
            person.description = reference.description
            person.url = reference.url
            person.email = reference.email
            person.telephone = reference.telephone
            person.save()
            reference.person = person
        reference.save()

class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0006_auto_20191011_0950'),
    ]

    operations = [
        migrations.RunPython(create_reference)
    ]
