from django.shortcuts import render
from django.http import HttpResponse

def login(request,username):

    return render(request,'login/login.html',context={"name":username})


def profile(request,username):
    return render(
        request,
        'login/profile.html',
        {'name':"mohammad",
         "age":31,
         "posts":10})