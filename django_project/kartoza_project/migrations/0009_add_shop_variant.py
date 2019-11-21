# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cartridge.shop.fields

TARGET_APP = 'shop'    # application label migration is for

class Migration(migrations.Migration):

    def __init__(self, name, app_label):
        # overriding application operated upon
        super(Migration, self).__init__(name, TARGET_APP)

    # specify what original migration file it replaces
    # or leave migration loader confused about unapplied migration
    replaces = ((TARGET_APP, __module__.rsplit('.', 1)[-1]),)

    dependencies = [
        ('shop', '0007_auto_20150921_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='option10',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True,
                                                    verbose_name=b'Time'),
        ),
    ]
