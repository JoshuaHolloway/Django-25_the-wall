# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-21 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0005_auto_20190621_0848'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
