# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='additional_info',
            field=models.TextField(default=b'', null=True, verbose_name='Additional Info', blank=True),
        ),
    ]
