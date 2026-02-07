from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") #when a user is deleted, all their notes are deleted as well
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) #automatically set the field to now every time the object is saved

    def __str__(self):
        return self.title