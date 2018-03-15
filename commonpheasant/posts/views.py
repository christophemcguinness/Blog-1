from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/index.html', {'posts': posts})

def post_details(request,post_id):
    post = get_object_or_404(Post, pk = post_id)
    #Post.objects.get(pk=post_id)
    return render(request, 'posts/posts_details.html', {'post': post})
