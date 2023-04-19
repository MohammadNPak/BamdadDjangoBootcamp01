from rest_framework import serializers
from accounts.models import UserProfile

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = ['id',]