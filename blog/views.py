from django.shortcuts import render
from django.views import generic
from blog.models import Author, Post, Comment

# Create your views here.
def index(request):
	posts = Post.objects.all()
	num_posts = Post.objects.all().count()
	num_authors = Author.objects.all().count()
	num_comments = Comment.objects.all().count()
	context = {
		'posts': posts,
		'num_posts': num_posts,
		'num_authors': num_authors,
		'num_comments': num_comments,

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