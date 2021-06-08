from django.db import models


class Image(models.Model):
    image_title = models.CharField(max_length=128)
    image = models.ImageField(upload_to= 'images/')

    def __str__(self):
            return self.image_title


class Post(models.Model):
    title = models.CharField(max_length=128)
    descriptions = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True)
    
    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'photos/')

    def __str__(self):
        return self.post.title
