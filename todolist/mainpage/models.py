from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    given = models.DateTimeField(default=datetime.now)
    deadline = models. DateTimeField(null=True)
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)
    category = models.CharField(default="#ff0000")
class Cat(models.Model):
    opisanie = models.CharField(max_length=512)
    catborn = models.DateTimeField()
    okras = models.CharField(max_length=512)
    poroda = models.CharField(max_length=512)
    namecat = models.CharField(max_length=512)
    polcat = models.BooleanField(default=False)


   