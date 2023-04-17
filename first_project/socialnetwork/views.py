from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from .models import Post,User,UserProfile
from .forms import CommentForm
# Create your views here.
from django.db.models import Count,OuterRef,Exists

@login_required
def post_list(request):
    
    posts = Post.objects.annotate(
        is_liked=Exists(UserProfile.objects.filter(
        user=request.user, like_set__id=OuterRef('pk')))).annotate(
        like_count=Count('like')).annotate(dislike_count=Count('dislike')).prefetch_related('author')

    if request.method == "GET":
        return render(request,'socialnetwork/post_list.html',context={'posts':posts})
    elif request.method == "POST":     
        new_post_body = request.POST["new_post_body"]
        new_post_title = request.POST["new_post_title"]
        Post.objects.create(
            body=new_post_body,
            author=request.user.userprofile,
            title=new_post_title)
        return render(request,'socialnetwork/post_list.html',context={'posts':posts})


@login_required
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.userprofile
            comment.save()
            
    return render(request,'socialnetwork/post_detail.html',{'post':post})

@login_required
def like_post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    user = request.user.userprofile
    if post.is_liked(user):
        post.like.remove(user)
    else:
        post.like.add(user)
        
    return redirect(reverse("post_list"))

