from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length= 255)
    password = models.CharField(max_length= 1024)
    bio = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
