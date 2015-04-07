# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdisplays', '0002_auto_20150406_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionfield',
            name='help_text',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
