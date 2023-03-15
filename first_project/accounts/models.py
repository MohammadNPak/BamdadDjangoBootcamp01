from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ps_choices = (
            ("D","Developer"),
            ("J","Junior Developer"),
            ("S","Senior Developer"),
            ("M","Manager"),
            ("T","Student"),
            ("I","Instructor"),
            ("N","Intern"),
            ("O","Other"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField('Skill')
    profile_picture =models.ImageField(upload_to='profile_pictures',default='profile_pictures\\default_profile_picture.png')
    bio = models.TextField()
    professional_status=models.CharField(max_length=1,choices=ps_choices)

    twitter = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)

    github_username = models.CharField(max_length=256,null=True,blank=True)
    location = models.CharField(max_length=128,null=True,blank=True)
    company = models.CharField(max_length=256,null=True,blank=True)
    website = models.URLField(null=True,blank=True)

    def __str__(self) -> str:
         return self.user.username+" | profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.bio
    except:
            UserProfile.objects.create(user=instance)


class Skill(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
         return self.name



class Experience(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    company = models.CharField(max_length=128)
    start = models.DateField()
    end = models.DateField(null=True,blank=True)
    is_continue = models.BooleanField(null=True,blank=True)
    position = models.CharField(max_length=256)
    Description = models.TextField()

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    University = models.CharField(max_length=256)
    start = models.DateField()
    end = models.DateField()
    degree = models.CharField(max_length=128)
    field_of_study = models.CharField(max_length=256)

    description = models.TextField()


class GithubRepos(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    Stars = models.IntegerField()
    Watchers = models.IntegerField()
    Forks = models.IntegerField()











