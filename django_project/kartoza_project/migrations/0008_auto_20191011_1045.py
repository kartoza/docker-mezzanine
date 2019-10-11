# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0007_auto_20191011_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_details',
        ),
        migrations.RemoveField(
            model_name='project',
            name='value',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='description',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='old_role',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='role_relation',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='url',
        ),
    ]
