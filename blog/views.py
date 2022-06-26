from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
	model = Post
	template_name = "post_list.html"


class PostCreateView(CreateView):
	model = Post	     
	fields = "__all__"
	success_url = reverse_lazy("blog:all")
	

class PostDetailView(DetailView):
	model = Post
	template_name = "post_detail.html"


class PostUpdateView(UpdateView):
	model = Post
	fields = "__all__"
	success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
	model = Post
	fields = "__all__"
	template_name = 'post_confirm_delete'
	success_url = reverse_lazy("blog:all")


# Create your views here
