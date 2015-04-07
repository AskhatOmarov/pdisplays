# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdisplays', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('description', models.ForeignKey(related_name='values', blank=True, to='pdisplays.Description', null=True)),
                ('section_field', models.ForeignKey(blank=True, to='pdisplays.SectionField', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sectionfield',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sectionfield',
            name='value',
        ),
        migrations.AlterField(
            model_name='sectionfield',
            name='section',
            field=models.ForeignKey(related_name='fields', blank=True, to='pdisplays.Section', null=True),
            preserve_default=True,
        ),
    ]
