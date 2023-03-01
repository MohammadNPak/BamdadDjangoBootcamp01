from django.shortcuts import render,get_object_or_404
from .models import Post,User

# Create your views here.

def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request,'socialnetwork/post_list.html',context={'posts':posts})
    
    elif request.method == "POST":
        # do something
       
        new_post_body = request.POST["new_post_body"]
        new_post_title = request.POST["new_post_title"]
        Post.objects.create(
            body=new_post_body,
            author=User.objects.get(id=1),
            title=new_post_title)


        posts = Post.objects.all()
        return render(request,'socialnetwork/post_list.html',context={'posts':posts})


def post_detail(request,pk):
  
    post = get_object_or_404(Post,pk=pk)
    return render(request,'socialnetwork/post_detail.html',{'post':post})
