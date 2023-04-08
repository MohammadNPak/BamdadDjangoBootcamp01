from django.urls import path
from socialnetwork.views import post_detail,post_list,like_post



urlpatterns = [
    path('',post_list,name='post_list'),
    path('post/<int:pk>',post_detail,name='post_detail'),
    path('like_post/<int:post_id>',like_post,name='like_post'),
]