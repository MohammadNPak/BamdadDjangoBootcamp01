from django.urls import path

from second_app import views
urlpatterns = [
    path('login/', views.login),
]