
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('paginas.urls')),
    url(r'^grafico_exibir/', include('paginas.urls'))    
]
