from django.urls import path
from accounts.views import login,register,logout,profile_detail,update_github,profile_list
from django.views.generic import TemplateView

urlpatterns=[
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('register-done/',
        TemplateView.as_view(template_name="accounts/register_done.html"),
        name='register_done'),
    path('logout-done',TemplateView.as_view(template_name="accounts/logout_done.html"),name="logout_done"),
    path('logout',logout,name='logout'),
    path('profile/<str:username>',profile_detail,name='profile_detail'),
    path('profiles',profile_list,name='profile_list'),
    path('updategithub',update_github,name='update_github'),
]