# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields
import mezzanine.utils.models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('mezzanine_people', '0002_add_mugshot_hover'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(related_name='user_link',
                                    verbose_name='UserLink',
                                    to=settings.AUTH_USER_MODEL,
                                    null=True),
        ),
    ]
