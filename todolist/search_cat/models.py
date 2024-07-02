from django.db import models


# Create your models here.
class Kitten(models.Model):
    opisanie = models.CharField(max_length=512)
    catborn = models.DateTimeField()
    okras = models.CharField(max_length=512)
    poroda = models.CharField(max_length=512)
    namecat = models.CharField(max_length=512)
    polcat = models.BooleanField(default=False)
    