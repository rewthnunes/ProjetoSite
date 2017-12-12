from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.pagina_exibir),
	url(r'^grafico_exibir', views.grafico_exibir, name='graph'),
]