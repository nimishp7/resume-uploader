from pyexpat import model
from rest_framework import serializers
from app.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        files = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage','rdoc']