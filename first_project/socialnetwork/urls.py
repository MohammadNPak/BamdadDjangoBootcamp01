from django.urls import path
from socialnetwork.views import explore,post_detail



urlpatterns = [
    path('',explore,name='explore'),
    path('post/<int:id>',post_detail,name='post_detail'),
]