# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0006_auto_20171030_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosSaoPaulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D1', models.CharField(max_length=1, verbose_name='D1 - Marutidade')),
            ],
        ),
    ]
