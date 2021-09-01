from django.shortcuts import render
from django.views import generic
from .models import Post 

# Create your views here.


# From build a blog app with django tutorial
# only published blog posts will appear on website
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'