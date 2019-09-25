# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0007_reference_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
