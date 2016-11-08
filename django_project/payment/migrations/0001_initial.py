# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField(verbose_name='Order Id')),
                ('bank_name', models.CharField(max_length=100, verbose_name='Bank Name')),
                ('bank_account', models.CharField(max_length=100, verbose_name='Bank Account')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('additional_info', models.TextField(default=b'', null=True, verbose_name='Additional Info')),
                ('status', models.IntegerField(default=1, verbose_name='Status', choices=[(1, b'Unchecked'), (2, b'Checked'), (3, b'Rejected')])),
            ],
        ),
    ]
