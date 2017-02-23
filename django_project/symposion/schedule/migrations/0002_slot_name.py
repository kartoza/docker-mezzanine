# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='name',
            field=models.CharField(default='default', max_length=100, editable=False),
        ),
    ]
