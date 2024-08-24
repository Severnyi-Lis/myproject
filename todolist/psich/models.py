from django.db import models
from datetime import datetime

# Create your models here.
class Psich(models.Model):
    name = models.CharField(max_length=512)
    surname = models.CharField(max_length=512)
    data = models.DateTimeField(default=datetime.now)
   