from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as django_login,logout as django_logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .models import GitRepoUpdateFail
# Create your views here.

def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            django_login(request,user=user)
            return redirect("post_list")
        else:
            messages.add_message(request, messages.ERROR,"Invalid Credentials")
            return render(request,'accounts/login.html',{})
    else:
        return render(request,'accounts/login.html',{})



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        u = User.objects.create(username=username,email=email)
        u.set_password(password1)
        u.save()
        return redirect("register_done")
    else:
        return render(request,'accounts/register.html',{})

def logout(request):
    django_logout(request)
    return redirect('logout_done')



def profile_detail(request,username):
    user_profile = get_object_or_404(UserProfile,user__username=username)
    return render(request,'accounts/profile_detail.html',{"profile":user_profile})

def profile_list(request):
    post_id = request.GET.get("post_id")
    print(dir(request))
    if post_id:
        profiles=UserProfile.objects.filter(like_set=post_id)
    else:
        profiles=UserProfile.objects.all()

    return render(request,"accounts/profile_list.html",{"profiles":profiles})

@login_required
def update_github(request):
    # print(request.user.username)
    try:
        request.user.userprofile.update_repos()
        messages.add_message(request,messages.SUCCESS,"repoes updated successfully!")

    except GitRepoUpdateFail:
        messages.add_message(request,messages.ERROR,"can not connect to github")
    # return redirect(reverse('post_list'))
    finally:
        return redirect(reverse('profile_detail',kwargs ={"username":request.user.username}))