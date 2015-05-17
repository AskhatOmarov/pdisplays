# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pdisplays', '0004_sectionfield_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='position',
            field=geoposition.fields.GeopositionField(default=b'0.0, 0.0', max_length=42),
            preserve_default=True,
        ),
    ]
