from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    