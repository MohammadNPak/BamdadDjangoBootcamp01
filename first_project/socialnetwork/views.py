from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,User

# Create your views here.

@login_required
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request,'socialnetwork/post_list.html',context={'posts':posts})
    
    elif request.method == "POST":     
        new_post_body = request.POST["new_post_body"]
        new_post_title = request.POST["new_post_title"]
        Post.objects.create(
            body=new_post_body,
            author=request.user.userprofile,
            title=new_post_title)
        posts = Post.objects.all()
        return render(request,'socialnetwork/post_list.html',context={'posts':posts})


@login_required
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'socialnetwork/post_detail.html',{'post':post})

