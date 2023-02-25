from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def explore(request):
    p = Post.objects.all()
    return render(request,'socialnetwork/explore.html',context={'posts':p})

def post_detail(request,id):
  
    p = get_object_or_404(Post,id=id)
    return render(request,'socialnetwork/post_detail.html',{'post':p})
