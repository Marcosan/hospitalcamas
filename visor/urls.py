from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

from hospitalview.viewsets import ZonaViewSet, HabitacionViewSet, CamaViewSet, EstadoViewSet, CamaEstadoViewSet, TipoCamaViewSet
from rest_framework.routers import DefaultRouter
#from apprest import viewsets

router = DefaultRouter()
router.register(r'zona',ZonaViewSet)
router.register(r'habitacion',HabitacionViewSet)
router.register(r'cama',CamaViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'cama_estado',CamaEstadoViewSet)
router.register(r'tipo_cama',TipoCamaViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'visor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    #url(r'^maps/', include('maps.urls')),
    url(r'^hospitalview/', include('hospitalview.urls')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
