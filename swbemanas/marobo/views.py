from django.views.generic.base import TemplateView
from django.shortcuts import render
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.list import ListView
#from django.core.urlresolvers import reverse_lazy
#from marobo.models import Population


class Index(TemplateView):
    template_name = 'marobo/index.html'
    

class Mapa(TemplateView):
    template_name = 'marobo/mapamarobo.html'
