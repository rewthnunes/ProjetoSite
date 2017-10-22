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
	github = models.CharField(max_length=100, default='https://github.com/seuGit', verbose_name='GitHub')
	current_position = models.CharField(max_length=100, default='Desenvolvedor', verbose_name='Cargo Atual')
	empresa = models.CharField(max_length=100, default='IFSP-CAMPINAS', verbose_name='Empresa')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Dados Pessoais'
		verbose_name_plural = 'Dados Pessoais'














