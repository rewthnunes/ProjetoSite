# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def pagina_exibir(request):
	return render(request, 'paginas/pagina_exibir.html', {})




