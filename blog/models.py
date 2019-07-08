from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	bio = models.TextField(max_length=500)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	class Meta:
		ordering = ['user']

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	def format_created_at(self):
		return self.created_at.strftime('%B, %-d, %Y')

	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.id)])

	class Meta:
		ordering = ['-created_at']

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.text

	def format_created_at(self):
		return self.created_at.strftime('%B, %-d, %Y, %H:%M')

	class Meta:
		ordering = ['created_at']