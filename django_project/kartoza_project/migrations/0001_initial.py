# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('clients', '0002_auto_20160907_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('short_description', models.TextField(null=True, verbose_name=b'Project short description', blank=True)),
                ('project_details', mezzanine.core.fields.RichTextField(null=True, verbose_name=b'Project details', blank=True)),
                ('thumbnail', models.ImageField(upload_to=b'project', null=True, verbose_name=b'Project thumbnail', blank=True)),
                ('date_start', models.DateField(null=True, blank=True)),
                ('date_end', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
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
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=300, null=True, blank=True)),
                ('project', models.ForeignKey(related_name='project_images', to='kartoza_project.Project')),
            ],
            bases=(mezzanine.utils.models.AdminThumbMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('project', models.ForeignKey(related_name='project_references', to='kartoza_project.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(related_name='project_category', null=True, verbose_name=b'Categories', to='kartoza_project.ProjectCategory', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='clients',
            field=models.ManyToManyField(related_name='clients', null=True, to='clients.Client', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
    ]
