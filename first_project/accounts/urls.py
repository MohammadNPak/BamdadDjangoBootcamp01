from django.urls import path
from accounts.views import login,register,logout
from django.views.generic import TemplateView

urlpatterns=[
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('register-done/',
        TemplateView.as_view(template_name="accounts/register_done.html"),
        name='register_done'),
    path('logout-done',TemplateView.as_view(template_name="accounts/logout_done.html"),name="logout_done"),
    path('logout',logout,name='logout'),
]