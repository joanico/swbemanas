from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    descriptions = HTMLField(blank=True, null=True)
    image = models.FileField(blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'photos/')
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    content = models.TextField()
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created_on',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)


class CommentPhoto(models.Model):
	image = models.ForeignKey(PostImage, on_delete = models.CASCADE)
	comment_post = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.author.username}\'s CommentPhoto- {self.author}'
