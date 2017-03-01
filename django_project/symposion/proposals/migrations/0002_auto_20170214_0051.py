# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalspeaker',
            options={'verbose_name': 'Additional speaker', 'verbose_name_plural': 'Additional speakers'},
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract',
            field=models.TextField(help_text=b"Will be made public if your proposal is accepted. Please aim for 125-175 words, 250 words is the maximum. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Detailed Abstract'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes',
            field=models.TextField(help_text="Anything else you'd like the program committee to know when making their selection: your past experience, etc. This is not made public. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Additional Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_speakers',
            field=models.ManyToManyField(to='symposion_speakers.Speaker', verbose_name='Additional speakers', through='symposion_proposals.AdditionalSpeaker', blank=True),
        ),
    ]
