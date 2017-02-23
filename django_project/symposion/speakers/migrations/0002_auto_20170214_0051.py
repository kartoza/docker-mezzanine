# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_speakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='company',
            field=models.CharField(help_text="The company/organisation/institution you'll be representing at the conference.", max_length=200, verbose_name='Company', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='biography',
            field=models.TextField(help_text='The biography won\'t be public, it may only be used by the session chairs to introduce you before your talk. Edit using <a href="http://daringfireball.net/projects/markdown/syntax" target=\'_blank\'>Markdown</a>.', verbose_name='Biography', blank=True),
        ),
    ]
