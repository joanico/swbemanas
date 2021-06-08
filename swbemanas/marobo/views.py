from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
#from django.views.generic.list import ListView
#from django.core.urlresolvers import reverse_lazy
from .models import Post, PostImage


def home(request):
    return render(request, "marobo/home.html")


class Mapa(TemplateView):
    template_name = 'marobo/mapamarobo.html'


class PopulationView(TemplateView):
    template_name = 'marobo/index.html'

    def get_context_data(self, **kwargs):
        context = super(PopulationView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        return context


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'marobo/index.html', {'posts':posts})

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'marobo/detail.html', {
        'post':post,
        'photos':photos
    })
