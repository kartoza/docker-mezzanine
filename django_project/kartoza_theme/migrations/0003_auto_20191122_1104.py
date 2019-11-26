# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_theme', '0002_auto_20191121_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='productviewdata',
            name='icon_background_color_hash',
            field=models.CharField(default=b'FFFFFF', max_length=6, verbose_name=b'Icon background color as 6 digit code'),
        ),
        migrations.AlterField(
            model_name='productviewdata',
            name='category_button_text',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Category button text'),
        ),
    ]
