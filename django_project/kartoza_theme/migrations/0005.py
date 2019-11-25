# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command
from django.core.management.commands import loaddata

class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_theme', '0004_productviewdata_category_order'),
    ]

    operations = [
        call_command(loaddata.Command(),
                     'kartoza_theme_initial.json',
                     verbosity=0)
    ]
