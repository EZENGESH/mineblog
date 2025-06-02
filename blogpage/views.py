from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blogpage/index.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blogpage/post_detail.html', {'post': post})
