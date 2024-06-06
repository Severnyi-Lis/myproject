from django.urls import path
from .views import index,new_task,new_cat
urlpatterns = [
    path('', index),
    path('newtask/',new_task, name='new_task'),
    path('cats/',new_cat, name='new_cat')
]