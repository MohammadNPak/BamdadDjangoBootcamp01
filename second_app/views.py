from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'second_app\login.html',{})