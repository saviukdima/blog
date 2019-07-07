from django.contrib import admin
from blog.models import Author, Post, Comment

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 0

class PostInline(admin.StackedInline):
	model = Post
	extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	model = Author
	list_display = ('user', 'bio')
	inlines = [PostInline]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ('title', 'body', 'author', 'created_at')
	inlines = [CommentInline]
	list_filter = ('author', 'created_at')

@admin.register(Comment)
class Comment(admin.ModelAdmin):
	model = Comment
	list_display = ('user', 'post', 'text', 'created_at')