from email.mime import image
from django.forms import SlugField
from django.template import context
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Post, PostImage, Comment
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import CommentForm
from django.views.generic.edit import FormMixin

# Profile view but did not use yet
def profile(request):
    return render(request, "marobo/profile.html")

def blog_view(request):
    # Get all data from Post database
    posts = Post.objects.all()
    return render(request, 'marobo/index.html', {'posts':posts})

class BlogDetail(FormMixin, DetailView):
    template_name= 'marobo/detail.html'
    model= Post
    Slug_Field = 'pk'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['blog'] = CommentForm(initial={'post': self.object})
        context['photos'] = PostImage.objects.filter(post=self.get_object())
        context['comments'] = Comment.objects.filter(post=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        photos = PostImage.objects.filter(post=post)
        comments = post.comments.filter(active=True, parent__isnull=True)
        if self.request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                parent_obj = None
                try:
                    parent_id = int(request.POST.get('parent_id'))
                except:
                    parent_id = None
                if parent_id:
                    parent_obj = Comment.objects.get(id=parent_id)
                    if parent_obj:
                        replay_comment = comment_form.save(commit=False)
                        replay_comment.parent = parent_obj
                new_comment = comment_form.save(commit=False)
                if request.user.is_authenticated:
                        new_comment.author = request.user
                elif  request.user.is_anonymous: # AnonymousUser code
                        new_comment.author = None
                new_comment.post = post
                new_comment.save()
                return HttpResponseRedirect(post.get_absolute_url())
        else:
            comment_form = CommentForm()
        return render(request, 'marobo/detail.html', {'post': post, 'photos': photos, 'comments': comments, 'comment_form': comment_form})


def detail_view(request, id):
    # get post object
    post = get_object_or_404(Post, id=id)
    # Filter images
    photos = PostImage.objects.filter(post=post)
    # list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True)
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
            elif  request.user.is_anonymous: # AnonymousUser code
                    new_comment.author = None
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            # return direct to absolute url
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, 'marobo/detail.html', {'post': post, 'photos':photos, 'comments': comments, 'comment_form': comment_form})

def login_view(request):
    # request post method
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
