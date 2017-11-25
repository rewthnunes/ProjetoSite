# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SaoPaulo(models.Model):
	name = models.CharField(max_length=50, default=' ',verbose_name='Nome')
	ano = models.CharField(max_length=04, default=' ',verbose_name='Ano Base')
	regiao = models.CharField(max_length=100, default=' ',verbose_name='Região')
	D1 = models.CharField(max_length=01, default='0', verbose_name='D1-Maturidade')
	D2 = models.CharField(max_length=01, default='0', verbose_name='D2-Comunicabilidade')
	D3 = models.CharField(max_length=01, default='0', verbose_name='D3-Disponibilidade')
	D4 = models.CharField(max_length=01, default='0', verbose_name='D4-Multiplicidade')
	D5 = models.CharField(max_length=01, default='0', verbose_name='D5-Acessibilidade')
	D6 = models.CharField(max_length=01, default='0', verbose_name='D6-Confiabilidade')
	D7 = models.CharField(max_length=01, default='0', verbose_name='D7-Usabilidade')
	D8 = models.CharField(max_length=01, default='0', verbose_name='D8-Transparência')
	D9 = models.CharField(max_length=01, default='0', verbose_name='D9-Prestação de Contas')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'São Paulo'
		verbose_name_plural = 'São Paulo'

#---------------------------------------------------------------------------------------------------














