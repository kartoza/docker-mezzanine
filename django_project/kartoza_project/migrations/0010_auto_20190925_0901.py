# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0009_auto_20190923_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcategory',
            name='site',
        ),
        migrations.RemoveField(
            model_name='project',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_details',
        ),
        migrations.RemoveField(
            model_name='project',
            name='value',
        ),
        migrations.AlterField(
            model_name='project',
            name='consultants',
            field=models.ManyToManyField(help_text=b'External company/individuals contracted to assist with the work done.', related_name='consultants', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='staff_involved',
            field=models.ManyToManyField(help_text=b'All kartoza staff who worked on this project.', related_name='staff_involved', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='person',
            field=models.ForeignKey(related_name='reference_person', to='kartoza_project.Person', null=True),
        ),
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
    ]
