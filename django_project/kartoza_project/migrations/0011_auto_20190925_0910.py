# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('kartoza_project', '0010_auto_20190925_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Project Category',
                'verbose_name_plural': 'Project Categories',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(related_name='project_category', null=True, verbose_name=b'Categories', to='kartoza_project.ProjectCategory', blank=True),
        ),
    ]
