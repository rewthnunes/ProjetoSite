# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import DadosPessoais, DadosSaoPaulo
from django.shortcuts import render

# Create your views here.

def pagina_exibir(request):

	pessoa = DadosPessoais.objects.all()
	context = {'pessoa': pessoa}
	return render(request, 'paginas/pagina_exibir.html', context)


	sp = DadosSaoPaulo.objects.all()
	contexty = {'sp': sp}
	return render(request, 'paginas/pagina_exibir.html', contexty)



