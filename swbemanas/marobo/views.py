from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from marobo.models import Potential


Class Create(CreateView):
    models = Population
    fields = ['distrito', 'sub_distrito', 'suco', 'aldeia']
    template_name = 'marobo/create.html'
    success_url = /reverse_lazy('index')
