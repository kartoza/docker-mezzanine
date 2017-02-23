# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_sponsorship', '0002_auto_20170214_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='content_type',
            field=models.CharField(default='simple', max_length=20, verbose_name='content type', choices=[('simple', 'Simple'), ('listing_text_en', 'Listing Text (English)'), ('listing_text_af', 'Listing Text (Afrikaans)'), ('listing_text_id', 'Listing Text (Indonesian)'), ('listing_text_ko', 'Listing Text (Korean)')]),
        ),
    ]
