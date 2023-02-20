from django.shortcuts import render

# Create your views here.

def explore(request):
    p1 = {
        # 'author_picture': https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fprofile%2F&psig=AOvVaw2ScT6HsSHutEEZGZeFFviK&ust=1676993113663000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCIiBsqi0pP0CFQAAAAAdAAAAABAE
        'author':'mohammad',
        'body':"hello this is my first post ",
        'title': 'first post',
        'date': '1401-12-1',
    }
    p2 = {
        # 'author_picture': https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fprofile%2F&psig=AOvVaw2ScT6HsSHutEEZGZeFFviK&ust=1676993113663000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCIiBsqi0pP0CFQAAAAAdAAAAABAE
        'author':'mohammad',
        'body':"hello this is my second post ",
        'title': 'second post',
        'date': '1401-12-1',
    }
    return render(request,'socialnetwork/explore.html',context={'posts':[p1,p2]})