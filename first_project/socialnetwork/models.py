from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =models.ImageField(upload_to='profile_pictures',default='profile_pictures\\default_profile_picture.png')
    bio = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(UserProfile(),on_delete=models.CASCADE)
    body = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    author = models.ForeignKey(UserProfile(),on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
