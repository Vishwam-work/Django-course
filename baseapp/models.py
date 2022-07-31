from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=255)
    disp=models.TextField(null=True,blank=True)
    # participants=
    updtaed = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        # this will order the new input data into the topmost order
        ordering=['-updtaed','-created']
    def __str__(self):
        return self.name
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    updtaed = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:50]



