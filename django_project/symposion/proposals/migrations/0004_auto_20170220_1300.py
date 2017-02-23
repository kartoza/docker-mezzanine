# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0003_auto_20170220_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract',
            field=models.TextField(help_text=b"Will be made public if your proposal is accepted. Please aim for 125-175 words, 250 words is the maximum. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Detailed Abstract'),
        ),
    ]
