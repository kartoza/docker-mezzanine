# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


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
            name='role',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='url',
        ),
        migrations.AddField(
            model_name='reference',
            name='person',
            field=models.ForeignKey(related_name='project_references', to='kartoza_project.Role', null=True),
        ),
    ]
