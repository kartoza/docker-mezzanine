# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qgis_mezzanine_model', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authlink',
            name='is_auth',
        ),
        migrations.AddField(
            model_name='authlink',
            name='show_after_login',
            field=models.BooleanField(default=True, verbose_name='Show After Login'),
        ),
        migrations.AddField(
            model_name='authlink',
            name='show_before_login',
            field=models.BooleanField(default=True, verbose_name='Show Before Login'),
        ),
    ]
