from django.test import TestCase
from django.urls import reverse

from blog.models import Author, Post, Comment
from django.contrib.auth.models import User

class PostListView(TestCase):
	@classmethod
	def setUpTestData(cls):
		number_of_posts = 12
		user = User.objects.create(username='test_user', email='test@test.com', password='1234')
		author = Author.objects.create(user=user)

		for post_id in range(number_of_posts):
			Post.objects.create(author=author)

	def test_post_list_view_url_exists_at_desired_location(self):
		response = self.client.get('/blog/blogs/')
		self.assertEquals(response.status_code, 200)

	def test_post_list_view_url_accessible_by_name(self):
		response = self.client.get(reverse('posts'))
		self.assertEquals(response.status_code, 200)

	def test_post_list_view_uses_correct_template(self):
		response = self.client.get(reverse('posts'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_list.html')	

	def test_posts_pagination_is_five(self):
		response = self.client.get(reverse('posts')+'?page=3')
		self.assertEquals(response.status_code, 200)
		self.assertTrue('is_paginated' in response.context)
		self.assertTrue(response.context['is_paginated'] == True)
		self.assertTrue(len(response.context['post_list']) == 2)