# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 23:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facerecognition', '0003_auto_20170815_2337'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fotos',
            new_name='Foto',
        ),
    ]
