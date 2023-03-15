from django.contrib import admin
from .models import Education,Experience,GithubRepos,Skill,UserProfile
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(GithubRepos)
admin.site.register(Skill)