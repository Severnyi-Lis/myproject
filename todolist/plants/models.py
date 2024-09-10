from django.db import models
 
# Create your models here.
class Rastenie(models.Model):
    name = models.CharField(max_length=512)
    cena = models.CharField(max_length=512)


class Dostavka(models.Model):
    kuda = models.CharField(max_length=512)
    tarif = models.CharField(max_length=512)

