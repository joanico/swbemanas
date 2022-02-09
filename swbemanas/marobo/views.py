from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Post, PostImage
from django.urls import reverse
from django.conf import settings


def home(request):
    return render(request, "marobo/home.html")

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
