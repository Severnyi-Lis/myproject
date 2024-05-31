from django.contrib import admin 
from .models import Task
from .models import Cat 
  
# Register your models here. 
 
@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Task._meta.get_fields()]
@admin.register(Cat) 
class CatAdmin(admin.ModelAdmin): 
    list_display_cat = [field.name for field in Cat._meta.get_fields()]