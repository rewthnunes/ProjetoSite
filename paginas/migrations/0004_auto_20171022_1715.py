# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_auto_20171022_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='github',
            field=models.CharField(default='https://github.com/seuGit', max_length=100, verbose_name='GitHub'),
        ),
    ]