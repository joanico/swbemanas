from django.contrib import admin
from .models import Post, PostImage, Comment, CommentPhoto

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'active', 'created_on']
    search_fields = ['content',]

@admin.register(CommentPhoto)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['image', 'comment_post', 'author', 'date_posted']
