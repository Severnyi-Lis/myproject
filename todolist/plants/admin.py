from django.contrib import admin
from .models import Rastenie
from .models import Dostavka

# Register your models here.
@admin.register(Rastenie) 
class RastenieAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Rastenie._meta.get_fields()]
@admin.register(Dostavka) 
class DostavkaAdmin(admin.ModelAdmin): 
    list_display_cat = [field.name for field in Dostavka._meta.get_fields()]