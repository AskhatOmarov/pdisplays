# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdisplays', '0005_display_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionfield',
            name='section',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.RemoveField(
            model_name='value',
            name='description',
        ),
        migrations.RemoveField(
            model_name='value',
            name='section_field',
        ),
        migrations.DeleteModel(
            name='SectionField',
        ),
        migrations.DeleteModel(
            name='Value',
        ),
        migrations.AddField(
            model_name='description',
            name='common_impression',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='content_relevance',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='crowd_coverage',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='indoor_outdoor',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Indoor', b'Indoor'), (b'Outdoor', b'Outdoor')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='input_formats',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'PAL', b'PAL'), (b'SECAM', b'SECAM'), (b'NTSC', b'NTSC'), (b'DVI', b'DVI'), (b'VGA', b'VGA')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='interaction_potential',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'LG', b'LG'), (b'Panasonic', b'Panasonic'), (b'Samsung', b'Samsung'), (b'Sony', b'Sony'), (b'Philips', b'Philips')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='mode_of_operation',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'part-time', b'Part-time'), (b'24/7', b'24/7')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='model',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='power_consumption',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='resolution',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'480p', b'480p (720 x 480)'), (b'720p', b'720p (1,280 x 720)'), (b'1080p', b'1080p (1,920 x 1,080)'), (b'4K UHD', b'4K UHD (3,840 x 2,160)'), (b'8K UHD', b'8K UHD (7,680 x 4,320)')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'small', b'Small: <50cm'), (b'medium', b'Medium: <1m'), (b'large', b'Large: <3m'), (b'extra-large', b'Extra-large: >3m')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='surroundings',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='total_score',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'LED', b'LED'), (b'LCD', b'LCD'), (b'PDP', b'PDP')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='viewing_distance',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='vision_quality',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='description',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='description',
            name='date_edited',
            field=models.DateTimeField(auto_now=True, max_length=100),
            preserve_default=True,
        ),
    ]
