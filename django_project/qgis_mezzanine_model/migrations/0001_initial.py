# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthLink',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('is_auth', models.BooleanField(default=False, verbose_name='Use Authentication')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Link Authentication',
                'verbose_name_plural': 'Link Authentications',
            },
            bases=('pages.page',),
        ),
    ]
