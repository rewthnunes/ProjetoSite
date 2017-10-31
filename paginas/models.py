# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DadosPessoais(models.Model):
	name = models.CharField(max_length=50, verbose_name='Nome')
	adress = models.CharField(max_length=100, verbose_name='Endereço')
	city = models.CharField(max_length=50, verbose_name='Cidade')
	cep = models.CharField(max_length=50, verbose_name='CEP')
	phone = models.CharField(max_length=20, verbose_name='Telefone')
	mobile = models.CharField(max_length=20, verbose_name='Celular')

	about = models.TextField(max_length=255, verbose_name='Sobre')
	data_nascimento = models.CharField(max_length=255, default='01 Janeiro 2017', verbose_name='Data Nascimento')
	email = models.EmailField(verbose_name='Email')

	conhecimentos = models.TextField(max_length=255, verbose_name='Conhecimentos')
	github = models.CharField(max_length=100, default='https://github.com/rewthnunes/ProjetoSite', verbose_name='GitHub')
	current_position = models.CharField(max_length=100, default='Desenvolvedor', verbose_name='Cargo Atual')
	empresa = models.CharField(max_length=100, default='IFSP-CAMPINAS', verbose_name='Empresa')


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Dados Pessoais'
		verbose_name_plural = 'Dados Pessoais'

#---------------------------------------------------------------------------------------------------

class DadosSaoPaulo(models.Model):
	capital = models.CharField(max_length=02, default='SP', verbose_name='Capital')
	ano = models.CharField(max_length=04, default='xxxx', verbose_name='Ano Base') 
	regiao = models.CharField(max_length=30, default='Sudeste', verbose_name='Região')
	D1 = models.CharField(max_length=01, default='0', verbose_name='D1 - Maturidade')
	D2 = models.CharField(max_length=01, default='0', verbose_name='D2 - Comunicabilidade')
	D3 = models.CharField(max_length=01, default='0', verbose_name='D3 - Disponibilidade')
	D4 = models.CharField(max_length=01, default='0', verbose_name='D4 - Multiplicidade Acesso')
	D5 = models.CharField(max_length=01, default='0', verbose_name='D5 - Acessibilidade')
	D6 = models.CharField(max_length=01, default='0', verbose_name='D6 - Confiabilidade')
	D7 = models.CharField(max_length=01, default='0', verbose_name='D7 - Usabilidade')
	D8 = models.CharField(max_length=01, default='0', verbose_name='D8 - Transparência')
	D9 = models.CharField(max_length=01, default='0', verbose_name='D9 - Prestação de Contas')


	#def __str__(self):
	#	return self.DadosSaoPaulo

	class Meta:
		verbose_name = 'Dados São Paulo'
		verbose_name_plural = 'Dados São Paulo'












