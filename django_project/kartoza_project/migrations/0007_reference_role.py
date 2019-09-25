# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0006_auto_20190923_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='role',
            field=models.ForeignKey(related_name='project_roles', to='kartoza_project.Role', null=True),
        ),
    ]
