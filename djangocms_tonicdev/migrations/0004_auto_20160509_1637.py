# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_tonicdev', '0003_auto_20160509_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='tonicnotebookpluginmodel',
            name='node_version',
            field=models.CharField(blank=True, help_text='Provide a semver range that the node engine should satisfy, e.g. 0.12.x or > 4.0.0', max_length=32, null=True, verbose_name=b'Node version'),
        ),
        migrations.AlterField(
            model_name='tonicnotebookpluginmodel',
            name='readonly',
            field=models.BooleanField(default=False, help_text='Create a notebook that can not be edited or run', verbose_name=b'Readonly'),
        ),
    ]
