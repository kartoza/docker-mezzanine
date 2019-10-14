# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0005_auto_20190719_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=10, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('telephone', models.CharField(help_text=b'Telephone number', max_length=16, blank=True)),
                ('email', models.EmailField(help_text=b'A contact email address for the reference', max_length=254, null=True, verbose_name=b'Email', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='role',
            new_name='old_role',
        ),
        migrations.AlterField(
            model_name='project',
            name='consultants',
            field=models.ManyToManyField(help_text=b'External company/individuals contracted to assist with the work done.', related_name='consultants', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project. As used in the world bank template.', verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='services_provided',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project. As used in the world bank template.', verbose_name=b'services_provided', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='staff_involved',
            field=models.ManyToManyField(help_text=b'All kartoza staff who worked on this project.', related_name='staff_involved', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='person',
            field=models.ForeignKey(related_name='reference_person', to='kartoza_project.Person', null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='role_relation',
            field=models.ForeignKey(related_name='reference_role', to='kartoza_project.Role', null=True),
        ),

    ]
