# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-22 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ygoDB', '0007_auto_20170522_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkmarker',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marker', to='ygoDB.CardStatus'),
        ),
    ]
