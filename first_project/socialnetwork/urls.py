from django.urls import path
from socialnetwork.views import explore



urlpatterns = [
    path('',explore,name='explore')
]