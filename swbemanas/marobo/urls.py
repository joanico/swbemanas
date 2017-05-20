from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='base'),
    url(r'^mapamarobo/$', views.Mapa.as_view(), name='mapamarobo'),
    url(r'^blog/$', views.Blog.as_view(), name='blog'),
]
