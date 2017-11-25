# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import SaoPaulo  
from django.shortcuts import render

# Create your views here.

def pagina_exibir(request):

	 sp = SaoPaulo.objects.all()
	 context = {'sp': sp}
	 return render(request, 'paginas/pagina_exibir.html', context)







