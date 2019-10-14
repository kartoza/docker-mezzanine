# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0008_auto_20191011_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='role_relation',
            field=models.ForeignKey(related_name='reference_role', to='kartoza_project.Role', null=True),
        ),
    ]
