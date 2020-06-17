from django.db import models

# Create your models here.

class Machine(models.Model):
    name = models.CharField(max_length=30)
    room = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

class Room(models.Model): 
    name = models.CharField(max_length=30)
    floor = models.IntegerField()
    capacity = models.IntegerField()
    room_map = models.FilePathField(path="")