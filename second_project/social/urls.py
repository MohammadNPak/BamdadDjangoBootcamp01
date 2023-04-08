from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('users/<int:pk>',ProfileView.as_view(),name="user_profile")
]
