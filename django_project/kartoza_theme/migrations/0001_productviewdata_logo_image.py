# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_theme', '0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='productviewdata',
            name='logo_image',
            field=models.ImageField(help_text=b"An image used as this product's logo", null=True, upload_to=b'product_image', blank=True),
        ),
    ]
