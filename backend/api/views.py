from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] #only authenticated users can access this view

    def get_queryset(self):
        user=self.request.user #only return notes that belong to the authenticated user
        return Note.objects.filter(user=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user) #set the user field to the authenticated user when creating a note
        else:
            print(serializer.errors) #print the validation errors if the serializer is not valid

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] #only authenticated users can access this view

    def get_queryset(self):
        user=self.request.user #only return notes that belong to the authenticated user
        return Note.objects.filter(user=user)
 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #make sure we dont have duplicate users, we can check the database for existing users
    serializer_class = UserSerializer #username and password are required fields, so we can use the User model to validate the data
    permission_classes = [AllowAny] #anyone can create a user, even if they are not authenticated

