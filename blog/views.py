from django.shortcuts import render
from django.views import generic
from blog.models import Author, Post, Comment
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

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
		'posts_by_user': posts_by_user
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

class CommentCreate(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ['text']

	def get_context_data(self, **kwargs):
		context = super(CommentCreate, self).get_context_data(**kwargs)
		context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
		return super(CommentCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse('post-detail', kwargs={'pk':self.kwargs['pk'],})