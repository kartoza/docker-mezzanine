# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20160908_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='bank_account',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='bank_name',
        ),
        migrations.AddField(
            model_name='payment',
            name='additional_document',
            field=models.FileField(max_length=255, upload_to=b'document', null=True, verbose_name='Additional Document', blank=True),
        ),
    ]
