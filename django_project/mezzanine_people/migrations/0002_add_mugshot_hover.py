# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields

class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mugshot_hover',
            field=mezzanine.core.fields.FileField(upload_to='people', null=True, verbose_name='Hover Profile photo', blank=True, max_length=200),
        ),
    ]
