from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.list import ListView
#from django.core.urlresolvers import reverse_lazy
#from marobo.models import Population


@login_required(login_url="login/")
def home(request):
    return render(request,"mapamarobo.html")


class Mapa(TemplateView):
    template_name = 'marobo/mapamarobo.html'
