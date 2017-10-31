# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0008_auto_20171030_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadossaopaulo',
            name='ano',
            field=models.CharField(default='xxxx', max_length=4, verbose_name='Ano Base'),
        ),
        migrations.AddField(
            model_name='dadossaopaulo',
            name='capital',
            field=models.CharField(default='SP', max_length=2, verbose_name='Capital'),
        ),
        migrations.AddField(
            model_name='dadossaopaulo',
            name='regiao',
            field=models.CharField(default='Sudeste', max_length=30, verbose_name='Regi\xe3o'),
        ),
    ]
