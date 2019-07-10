from django.test import TestCase
from blog.models import Author, Post, Comment
from django.contrib.auth.models import User

class AuthorModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(username='test_user', email='test@test.com', password='1234')
		Author.objects.create(user=user)

	def test_user_label(self):
		author = Author.objects.get(id=1)
		field_label = author._meta.get_field('user').verbose_name
		self.assertEquals(field_label, 'user')

	def test_bio_label(self):
		author = Author.objects.get(id=1)
		field_label = author._meta.get_field('bio').verbose_name
		self.assertEquals(field_label, 'bio')

	def test_bio_max_length(self):
		author = Author.objects.get(id=1)
		max_length = author._meta.get_field('bio').max_length
		self.assertEquals(max_length, 500)

	def test_get_absolute_url(self):
		author = Author.objects.get(id=1)
		self.assertEquals(author.get_absolute_url(), '/blog/blogger/1/')

class PostModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(username='test_user', email='test@test.com', password='1234')
		author = Author.objects.create(user=user)
		Post.objects.create(author=author, title='title for test')

	def test_title_label(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')

	def test_body_label(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('body').verbose_name
		self.assertEquals(field_label, 'body')

	def test_created_at_label(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('created_at').verbose_name
		self.assertEquals(field_label, 'created at')

	def test_title_max_length(self):
		post = Post.objects.get(id=1)
		max_length = post._meta.get_field('title').max_length
		self.assertEquals(max_length, 100)

	def test_str_method(self):
		post = Post.objects.get(id=1)
		self.assertEquals(str(post), post.title)

	def test_post_get_absolute_url(self):
		post = Post.objects.get(id=1)
		self.assertEquals(post.get_absolute_url(), '/blog/1/')

class CommentModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		user_by_user_model = User.objects.create(username='test_user', email='test@test.com', password='1234')
		user = user_by_user_model
		author_of_post = Author.objects.create(user=user_by_user_model)
		post = Post.objects.create(author=author_of_post)
		Comment.objects.create(user=user, post=post, text='test text')

	def test_user_label(self):
		comment = Comment.objects.get(id=1)
		field_label = comment._meta.get_field('user').verbose_name
		self.assertEquals(field_label, 'user')

	def test_text_label(self):
		comment = Comment.objects.get(id=1)
		field_label = comment._meta.get_field('text').verbose_name
		self.assertEquals(field_label, 'text')

	def test_str_method(self):
		comment = Comment.objects.get(id=1)
		self.assertEquals(str(comment), comment.text)