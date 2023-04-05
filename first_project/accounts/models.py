from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class GitRepoUpdateFail(Exception):
    pass

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

    github_username = models.CharField(max_length=256)
    location = models.CharField(max_length=128,null=True,blank=True)
    company = models.CharField(max_length=256,null=True,blank=True)
    website = models.URLField(null=True,blank=True)

    def __str__(self) -> str:
         return self.user.username+" | profile"

    def update_repos(self):
        response = requests.get(f"https://api.github.com/users/{self.github_username}/repos")
        if response.status_code==200:
            repos = response.json()
            github_repos_objects = []
            for repo in repos:
                title = repo["name"]
                description = repo["description"]
                url = repo["url"]
                Forks = repo["forks_count"]
                Stars = repo["stargazers_count"]
                Watchers = repo["watchers_count"]
                github_repos_objects.append(
                    GithubRepos(
                        user_profile=self,
                        title=title,
                        description=description,
                        Forks=Forks,
                        Stars=Stars,
                        Watchers=Watchers))
            GithubRepos.objects.filter(user_profile=self).delete()
            GithubRepos.objects.bulk_create(github_repos_objects)

        else:
            raise GitRepoUpdateFail("can not connect to github or invalid username!")
         


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.bio
    except:
        UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=UserProfile)
# def create_github_repos(sender, instance, **kwargs):
#     try:
#         instance.gihub_username
#     except:
#         instance.update_repos()
        

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
    description = models.TextField()
    def __str__(self) -> str:
         return f"Experience | {self.user_profile.user.username}"

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    university = models.CharField(max_length=256)
    start = models.DateField()
    end = models.DateField()
    degree = models.CharField(max_length=128)
    field_of_study = models.CharField(max_length=256)

    description = models.TextField()

    def __str__(self) -> str:
         return f"Education | {self.user_profile.user.username}"


import requests
class GithubRepos(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField(null=True)
    Stars = models.IntegerField(default=0)
    Watchers = models.IntegerField(default=0)
    Forks = models.IntegerField(default=0)








