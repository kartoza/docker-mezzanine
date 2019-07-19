# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0004_auto_20190711_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.CharField(help_text=b'In which country was the project located', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(help_text=b'Where was the project located more specifically', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Project short description', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(help_text=b'Comma seperated list of keywords associated with the project', max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.CharField(help_text=b'Comma seperated list of technologies associated with the project', max_length=1000, null=True, blank=True),
        ),
    ]
