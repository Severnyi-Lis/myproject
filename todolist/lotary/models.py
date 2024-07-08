from django.db import models

# Create your models here.
class Wins(models.Model):
    name = models.CharField(max_length=512)
    surname = models.CharField(max_length=512)
    summa_of_wins = models.CharField(max_length=512)
    