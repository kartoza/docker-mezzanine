# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
         ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductViewData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_summary', models.CharField(max_length=255, verbose_name=b'Category Page Summary')),
                ('category_html', models.TextField(verbose_name=b'Category Page HTML')),
                ('product', models.ForeignKey(related_name='project_images', to='shop.Product')),
            ],
        ),
    ]
