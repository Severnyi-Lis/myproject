from django.contrib import admin

# Register your models here.
from .models import Psich

# Register your models here.
@admin.register(Psich) 
class PsichAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Psich._meta.get_fields()]