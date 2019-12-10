# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description_summary',
        ),
        migrations.RemoveField(
            model_name='project',
            name='services_provided_summary',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='description',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='old_role',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='url',
        ),
        migrations.AlterField(
            model_name='project',
            name='github_page',
            field=models.URLField(help_text=b"A link to the project's github page.", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='services_provided',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project. As used in the world bank template.', verbose_name=b'services_provided', blank=True),
        ),
    ]
