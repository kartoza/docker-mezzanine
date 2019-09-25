# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0008_person_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='person',
            field=models.ForeignKey(related_name='reference_person', to='kartoza_project.Role', null=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='role',
            field=models.ForeignKey(related_name='reference_role', to='kartoza_project.Role', null=True),
        ),
    ]
