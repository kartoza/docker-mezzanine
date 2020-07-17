# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django_countries import countries


def move_countries(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.

    Project = apps.get_model('kartoza_project', 'Project')

    for project in Project.objects.all():
        if len(project.country) > 0:
            try:
                project.country_iso = get_iso_country_by_name(project.country)

            except Exception:
                project.location = '{country} {location}'.format(
                    country=project.country, location=project.location)
            project.save()


def unmove_countries(apps, schema_editor):
    Project = apps.get_model('kartoza_project', 'Project')

    for project in Project.objects.all():
        if len(project.country) > 0:
            project.country_iso = None
            project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0011_project_country_iso'),
    ]

    operations = [
        migrations.RunPython(move_countries, unmove_countries),
        migrations.RemoveField(
            model_name='project',
            name='country',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='country_iso',
            new_name='country',
        ),
    ]


def get_iso_country_by_name(name):
    for country in countries:
        if name == country[1]:
            return country
    return None