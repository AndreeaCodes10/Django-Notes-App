from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #no one can see the password when we get the user data, but we can set it when we create a user

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "user", "title", "content", "created_at", "updated_at"]
        extra_kwargs = {"user": {"read_only": True}, "created_at": {"read_only": True}, "updated_at": {"read_only": True}} #the user field will be set automatically to the authenticated user, and the created_at and updated_at fields will be set automatically by the model
        