# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the client.', max_length=255)),
                ('description', mezzanine.core.fields.RichTextField(default=b'', help_text='A description for the client', max_length=500, verbose_name='description', blank=True)),
                ('link', models.URLField(help_text='Client company site link', max_length=255)),
                ('logo', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Client logo image', blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('name', 'link', 'logo', 'description'),
                'verbose_name': 'Clients',
                'verbose_name_plural': 'Client',
            },
        ),
    ]
