from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
  CreateView, 
  UpdateView,
  DeleteView
)
from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class BlogListView(ListView):
  model = Post
  template_name = 'index.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class BlogCreateNew(CreateView):
  model = Post
  template_name = 'create_post.html'
  fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
  model = Post
  template_name = 'edit_post.html'
  fields = ['title', 'body']

class BlogDeleteView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')
