# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0002_project_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('_order',)},
        ),
        migrations.AddField(
            model_name='project',
            name='_order',
            field=mezzanine.core.fields.OrderField(null=True, verbose_name='Order'),
        ),
    ]
