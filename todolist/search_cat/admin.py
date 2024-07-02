from django.contrib import admin
from .models import Kitten

# Register your models here.
@admin.register(Kitten) 
class KittenAdmin(admin.ModelAdmin): 
    list_display_cat = [field.name for field in Kitten._meta.get_fields()]