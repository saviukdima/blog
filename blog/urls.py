from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('blogs/', views.PostListView.as_view(), name='posts'),
	path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
	path('bloggers/', views.AuthorListView.as_view(), name='authors'),
	path('blogger/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
	path('myposts/', views.PostsByUserListView.as_view(), name='my-posts'),
]
