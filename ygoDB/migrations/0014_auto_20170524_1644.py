# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-24 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygoDB', '0013_auto_20170522_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackList',
            fields=[
                ('pack_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='pack_id')),
                ('pack_name', models.CharField(max_length=255, unique=True, verbose_name='pack_name')),
            ],
        ),
        migrations.AlterField(
            model_name='cardstatus',
            name='race',
            field=models.CharField(blank=True, choices=[('ドラゴン', 'ドラゴン族'), ('魔法使い', '魔法使い族'), ('アンデット', 'アンデット族'), ('戦士', '戦士族'), ('獣戦士', '獣戦士族'), ('獣', '獣族'), ('鳥獣', '鳥獣族'), ('悪魔', '悪魔族'), ('天使', '天使族'), ('昆虫', '昆虫族'), ('恐竜', '恐竜族'), ('爬虫類', '爬虫類族'), ('魚', '魚族'), ('海竜', '海竜族'), ('機械', '機械族'), ('雷', '雷族'), ('水', '水族'), ('炎', '炎族'), ('岩石', '岩石族'), ('植物', '植物族'), ('サイキック', 'サイキック族'), ('幻竜', '幻竜族'), ('サイバース', 'サイバース族'), ('幻神獣', '幻神獣族'), ('創造神', '創造神族')], max_length=10, null=True, verbose_name='race'),
        ),
        migrations.AlterField(
            model_name='linkmarker',
            name='marker',
            field=models.IntegerField(choices=[(0, '左上'), (1, '上'), (2, '右上'), (3, '左'), (4, '中央'), (5, '右'), (6, '左下'), (7, '下'), (8, '右下')], primary_key=True, serialize=False, verbose_name='marker'),
        ),
        migrations.AlterField(
            model_name='pendulumstatus',
            name='pendulum_effect',
            field=models.TextField(blank=True, null=True, verbose_name='pendulum_effect'),
        ),
    ]