from django.shortcuts import render
from django.views.generic import DetailView

from social.models import Profile
# Create your views here.


class ProfileView(DetailView):
    model=Profile
    template_name='social/profile_detail.html'



