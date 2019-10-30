# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0009_auto_20191023_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location_point',
            field=django.contrib.gis.db.models.fields.PointField(help_text=b"The location's point coordinate", srid=4326, null=True, blank=True),
        ),
    ]
