from django.contrib import admin
from .models import Wins

# Register your models here.
@admin.register(Wins) 
class WinsAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Wins._meta.get_fields()]