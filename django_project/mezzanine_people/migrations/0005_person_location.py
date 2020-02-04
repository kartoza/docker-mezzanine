# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_people', '0004_auto_20191203_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
    ]
