from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,'socialnetwork/post_list.html',context={'posts':posts})

def post_detail(request,pk):
  
    post = get_object_or_404(Post,pk=pk)
    return render(request,'socialnetwork/post_detail.html',{'post':post})
