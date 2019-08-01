# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20160914_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField(verbose_name=b'Order Id')),
                ('vat_number', models.CharField(help_text=b'South African Registered vat number', max_length=10)),
            ],
        ),
    ]
