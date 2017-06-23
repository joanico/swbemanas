from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^mapamarobo/$', views.Mapa.as_view(), name='mapamarobo'),
]
