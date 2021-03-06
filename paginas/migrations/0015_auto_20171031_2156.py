# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0014_auto_20171031_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saopaulo',
            name='about',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='conhecimentos',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='current_position',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='github',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='saopaulo',
            name='phone',
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D1',
            field=models.CharField(default='0', max_length=1, verbose_name='D1-Maturidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D2',
            field=models.CharField(default='0', max_length=1, verbose_name='D2-Comunicabilidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D3',
            field=models.CharField(default='0', max_length=1, verbose_name='D3-Disponibilidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D4',
            field=models.CharField(default='0', max_length=1, verbose_name='D4-Multiplicidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D5',
            field=models.CharField(default='0', max_length=1, verbose_name='D5-Acessibilidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D6',
            field=models.CharField(default='0', max_length=1, verbose_name='D6-Confiabilidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D7',
            field=models.CharField(default='0', max_length=1, verbose_name='D7-Usabilidade'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D8',
            field=models.CharField(default='0', max_length=1, verbose_name='D8-Transpar\xeancia'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='D9',
            field=models.CharField(default='0', max_length=1, verbose_name='D9-Presta\xe7\xe3o de Contas'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='ano',
            field=models.CharField(default=' ', max_length=4, verbose_name='Ano Base'),
        ),
        migrations.AddField(
            model_name='saopaulo',
            name='regiao',
            field=models.CharField(default=' ', max_length=100, verbose_name='Regi\xe3o'),
        ),
        migrations.AlterField(
            model_name='saopaulo',
            name='name',
            field=models.CharField(default=' ', max_length=50, verbose_name='Nome'),
        ),
    ]
