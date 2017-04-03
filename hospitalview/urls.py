from django.conf.urls import patterns, url

# media files
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hospitalview import views

urlpatterns = patterns('',
    url(r'^camas/$', views.CamasView, name='camas'),
    url(r'^camasedit/$', views.CamasEdit, name='camasedit'),
    url(r'^zonas/$', views.ZonasView, name='zonas'),
    url(r'^panel/$', views.PanelView, name='panel'),
	url(r'^camasjson/', views.getCamasEstadoJson, name='camasestado'),
	url(r'^zonasjson/', views.getZonasEstadoJson, name='zonasestado'),
	url(r'^contestadosjson/', views.getContEstadosJson, name='contestados'),
	url(r'^postEstadosCama/', views.postEstadosCama, name='postEstadosCama'),
	url(r'^postCamaEstado/', views.postCamaEstado, name='postCamaEstado'),
	url(r'^postReservado/', views.postReservado, name='postReservado'),
	url(r'^postInhabilitado/', views.postInhabilitado, name='postInhabilitado'),

    #url(r'^coordenadas', views.coordenadas, name='coordenadas'),

) 

#urlpatterns += staticfiles_urlpatterns()
