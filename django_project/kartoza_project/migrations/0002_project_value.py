# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='value',
            field=models.DecimalField(null=True, verbose_name=b'Project value', max_digits=10, decimal_places=2, blank=True),
        ),
    ]
