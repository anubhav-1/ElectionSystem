# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_card', '0010_auto_20170704_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='state_id',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='grampanchayat',
            name='tehsil_id',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='person',
            name='gram_panchayat_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tehsil',
            name='district_id',
            field=models.CharField(max_length=6),
        ),
    ]
