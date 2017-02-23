# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_sponsorship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='contact_email',
            field=models.EmailField(max_length=254, verbose_name='Contact Email', blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='contact_name',
            field=models.CharField(max_length=100, verbose_name='Contact Name', blank=True),
        ),
    ]
