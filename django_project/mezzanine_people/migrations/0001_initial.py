# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields
import mezzanine.utils.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', db_index=True, blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=100, verbose_name='last name', blank=True)),
                ('mugshot', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Profile photo', blank=True)),
                ('mugshot_hover', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Hover Profile photo', blank=True)),
                ('mugshot_credit', models.CharField(max_length=200, verbose_name='Profile photo credit', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail address', blank=True)),
                ('bio', mezzanine.core.fields.RichTextField(default=b'', help_text='This field can contain HTML and should contain a few paragraphs describing the background of the person.', verbose_name='biography', blank=True)),
                ('job_title', models.CharField(help_text='Example: First Grade Teacher', max_length=60, verbose_name='job title', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ('order', 'last_name', 'first_name'),
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Person Category',
                'verbose_name_plural': 'Person Categories',
            },
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Friendly name of the link. E.g. Twitter', max_length=50, verbose_name='link name')),
                ('url', models.URLField(verbose_name='URL')),
                ('person', models.ForeignKey(to='mezzanine_people.Person')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='person',
            name='categories',
            field=models.ManyToManyField(related_name='people', verbose_name='Categories', to='mezzanine_people.PersonCategory', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(related_name='user_link', verbose_name='UserLink', to=settings.AUTH_USER_MODEL),
        ),
    ]
