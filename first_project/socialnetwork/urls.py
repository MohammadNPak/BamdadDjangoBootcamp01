from django.urls import path
from socialnetwork.views import post_detail,post_list



urlpatterns = [
    path('',post_list,name='post_list'),
    path('post/<int:pk>',post_detail,name='post_detail'),
]