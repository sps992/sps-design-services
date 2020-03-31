# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-31 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20200322_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetails',
            name='amendments',
            field=models.CharField(blank=True, choices=[('Amendments: 3', '3'), ('Amendments: 5', '5'), ('Amendments: 7', '7'), ('Amendments: UNLIMITED', 'UNLIMITED'), (' ', ' ')], default='', max_length=254, null=True),
        ),
    ]
