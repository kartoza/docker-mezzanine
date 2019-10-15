# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0005_auto_20190719_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_details',
        ),
        migrations.RemoveField(
            model_name='project',
            name='value',
        ),
        migrations.AddField(
            model_name='project',
            name='description_summary',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should briefly describe work done during the project. For exporting to public documents.', verbose_name=b'description_summary', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='services_provided_summary',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should briefly describe services provided during the project. For exporting to public documents. Maximum of 160 words or 27 lines', verbose_name=b'services_provided_summary', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='consultants',
            field=models.ManyToManyField(help_text=b'External company/individuals contracted to assist with the work done.', related_name='consultants', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project. As used in the world bank template.', verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_page',
            field=models.URLField(help_text=b"A link to the project's g  ithub page.", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='services_provided',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project. As used in the world bank template. Maximum of 250 words or 27 lines', verbose_name=b'services_provided', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='staff_involved',
            field=models.ManyToManyField(help_text=b'All kartoza staff who worked on this project.', related_name='staff_involved', null=True, to='kartoza_project.Reference', blank=True),
        ),
    ]
