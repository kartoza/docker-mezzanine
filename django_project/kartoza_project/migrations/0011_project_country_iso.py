# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0010_project_location_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='country_iso',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]