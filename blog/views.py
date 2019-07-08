from django.shortcuts import render
from django.views import generic
from blog.models import Author, Post, Comment
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
	posts = Post.objects.all()
	num_posts = Post.objects.all().count()
	num_authors = Author.objects.all().count()
	num_comments = Comment.objects.all().count()

	num_posts_by_user = Post.objects.filter(author=request.user.id).count()
	posts_by_user = Post.objects.filter(author=request.user.id)

	context = {
		'posts': posts,
		'num_posts': num_posts,
		'num_authors': num_authors,
		'num_comments': num_comments,
		'num_posts_by_user': num_posts_by_user,
		'posts_by_user': posts_by_user,
	}
	return render(request, 'index.html', context=context)

class PostListView(generic.ListView):
	model = Post
	paginate_by = 5

class PostDetailView(generic.DetailView):
	model = Post

class AuthorListView(generic.ListView):
	model = Author

class AuthorDetailView(generic.DetailView):
	model = Author

class PostsByUserListView(LoginRequiredMixin, generic.ListView):
	model = Post
	template_name = 'blog/posts_by_user.html'

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user.id)