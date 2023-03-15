from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request,'socialnetwork/post_list.html',context={'posts':posts})

@login_required
def post_detail(request,pk):
    p = get_object_or_404(Post,pk=pk)
    return render(request,'socialnetwork/post_detail.html',{'post':p})
