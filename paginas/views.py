# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import SaoPaulo, Populacao 
from django.shortcuts import render

# Create your views here.

def pagina_exibir(request):

	 sp = SaoPaulo.objects.all() 
	 hb = Populacao.objects.all()
	 context	 = {'sp': sp, 'hb': hb}
	 
	 return render(request, 'paginas/pagina_exibir.html', context)

def grafico_exibir(request):

	 sp = SaoPaulo.objects.all() 
	 hb = Populacao.objects.all()
	 context	 = {'sp': sp, 'hb': hb}
	 
	 return render(request, 'paginas/grafico_exibir.html', context)





