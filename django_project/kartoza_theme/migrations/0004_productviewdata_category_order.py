# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_theme', '0003_auto_20191122_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='productviewdata',
            name='category_order',
            field=models.IntegerField(default=0, verbose_name=b'Order the item should displayed on the category page'),
        ),
    ]
