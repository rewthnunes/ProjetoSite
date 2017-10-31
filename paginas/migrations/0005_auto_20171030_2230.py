# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_auto_20171022_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesquisaSaoPaulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.CharField(max_length=2, verbose_name='Dimens\xe3o 1')),
            ],
            options={
                'verbose_name': 'Dados Pessoais',
                'verbose_name_plural': 'Dados Pessoais',
            },
        ),
        migrations.AlterModelOptions(
            name='dadospessoais',
            options={},
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='github',
            field=models.CharField(default='https://github.com/rewthnunes/ProjetoSite', max_length=100, verbose_name='GitHub'),
        ),
    ]
