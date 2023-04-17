from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import UserProfile

             
from django import template
register = template.Library()

class Post(models.Model):
    author = models.ForeignKey(UserProfile(),on_delete=models.CASCADE)
    body = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(UserProfile,related_name="like_set",blank=True,null=True)
    dislike =  models.ManyToManyField(UserProfile,related_name="dislike_set",blank=True,null=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def is_liked(self,user_profile):
        return self.like.filter(id=user_profile.id).count()==1

class Comment(models.Model):
    author = models.ForeignKey(UserProfile(),on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
