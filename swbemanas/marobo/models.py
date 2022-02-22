from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=128)
    descriptions = HTMLField(blank=True, null=True)
    image = models.FileField(blank=True)
    
    def __str__(self):
        return self.title


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
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created_on',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
