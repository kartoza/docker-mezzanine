# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command
from django.core.management.commands import loaddata


def load_data(apps, schema_editor):
    call_command('loaddata',
                 'kartoza_theme_initial.json',
                 verbosity=0)

class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_theme', '0004_productviewdata_category_order'),
    ]

    operations = [
        migrations.RunPython(load_data),

    ]
