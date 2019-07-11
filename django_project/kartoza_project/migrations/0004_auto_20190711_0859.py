# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kartoza_project', '0003_auto_20190709_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approximate_contract_value',
            field=models.IntegerField(help_text=b'Approximate value of the contract (US $)', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='consultants',
            field=models.ManyToManyField(related_name='consultants', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='contact_person',
            field=models.ForeignKey(related_name='contact_person', on_delete=django.db.models.deletion.PROTECT, to='kartoza_project.Reference', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.TextField(help_text=b'In which country was the project located', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project.', verbose_name=b'description', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='duration_of_assignment',
            field=models.IntegerField(help_text=b'Duration of the assignment (months).', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='github_page',
            field=models.URLField(help_text=b"A link to the project's github page.", max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.TextField(help_text=b'Where was the project located more specifically', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='public_page',
            field=models.URLField(help_text=b'If available to the public, where can the project be found?', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='published',
            field=models.BooleanField(default=False, verbose_name=b'Published to public gallery'),
        ),
        migrations.AddField(
            model_name='project',
            name='services_provided',
            field=mezzanine.core.fields.RichTextField(default=b'', help_text=b'This field can contain HTML and should contain a few paragraphs describing the background of the project.', verbose_name=b'services_provided', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='staff_involved',
            field=models.ManyToManyField(related_name='staff_involved', null=True, to='kartoza_project.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.TextField(help_text=b'Comma seperated list of keywords associated with the project', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.TextField(help_text=b'Comma seperated list of technologies associated with the project', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='total_staff_months',
            field=models.IntegerField(help_text=b'Total number of staff-months required to complete the project.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='total_staff_months_by_kartoza',
            field=models.IntegerField(help_text=b'Number of professional staff-months provided by Kartoza.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='email',
            field=models.EmailField(help_text=b'A contact email address for the reference', max_length=254, null=True, verbose_name=b'Email', blank=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='role',
            field=models.CharField(help_text=b'Role in the project', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='telephone',
            field=models.CharField(help_text=b'Telephone number', max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(help_text=b'An image associated with a Kartoza project', upload_to=b'project_image', blank=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='project',
            field=models.ForeignKey(related_name='project_references', to='kartoza_project.Project', null=True),
        ),
    ]
