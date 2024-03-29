from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Post, PostImage, Comment
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage 

# Profile view but did not use yet
def profile(request):
    return render(request, "marobo/profile.html")

def blog_view(request):
    # Get all data from Post database
    posts = Post.objects.all()
    return render(request, 'marobo/index.html', {'posts':posts})

def detail_view(request, id):
    # get post object
    post = get_object_or_404(Post, id=id)
    # Filter images
    photos = PostImage.objects.filter(post=post)
    # list of active parent comments
    page = request.GET.get('page', 1)
    paginator = Paginator(photos, 6)
    comments = post.comments.filter(active=True, parent__isnull=True)
    try:
        photos = paginator.page(page)
    except InvalidPage:
        # if the page contains no results (EmptyPage exception) or
        # the page number is not an integer (PageNotAnInteger exception)
        # return the first page
        photos = paginator.page(1)

    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # set default for user who are logged create comment
            if request.user.is_authenticated:
                    new_comment.author = request.user
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            # return direct to absolute url
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, 'marobo/detail.html', {'post': post, 'photos':photos, 'comments': comments, 'comment_form': comment_form})


def login_view(request, *args, **kwargs):
    redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
    # request post method
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(redirect_to)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
