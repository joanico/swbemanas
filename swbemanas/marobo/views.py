from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
#from django.views.generic.list import ListView
#from django.core.urlresolvers import reverse_lazy
from .models import Suco, Population, Aldeia


def home(request):
    return render(request, "marobo/home.html")


class Mapa(TemplateView):
    template_name = 'marobo/mapamarobo.html'


class PopulationView(TemplateView):
    template_name = 'marobo/suco.html'

    def get_context_data(self, **kwargs):
        context = super(PopulationView, self).get_context_data(**kwargs)
        context['sucos'] = Suco.objects.all().order_by('name')
        context['populations'] = Population.objects.all()
        context['aldeias'] = Aldeia.objects.all()
        return context
