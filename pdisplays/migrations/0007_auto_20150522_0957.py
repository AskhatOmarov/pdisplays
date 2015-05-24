# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdisplays', '0006_auto_20150517_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, help_text=b'Evaluate size of the display', choices=[(b'small', b'Small: <50cm'), (b'medium', b'Medium: <1m'), (b'large', b'Large: <3m'), (b'extra-large', b'Extra-large: >3m')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='description',
            name='total_score',
            field=models.IntegerField(blank=True, max_length=100, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
    ]
