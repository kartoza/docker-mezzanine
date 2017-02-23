# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0002_auto_20170214_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract',
            field=models.TextField(help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Detailed Abstract'),
        ),
    ]
