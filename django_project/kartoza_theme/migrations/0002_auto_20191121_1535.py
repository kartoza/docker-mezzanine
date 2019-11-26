# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_theme', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productviewdata',
            options={'verbose_name_plural': 'Product View Data'},
        ),
        migrations.AddField(
            model_name='productviewdata',
            name='category_button_text',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Category Page Summary'),
        ),
    ]
