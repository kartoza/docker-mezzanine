# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_people', '0003_add_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mugshot_hover',
            field=mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Hover Profile photo', blank=True),
        ),
    ]
