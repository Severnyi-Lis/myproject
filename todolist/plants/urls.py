from django.urls import path
from .views import plants
urlpatterns = [
    path('', plants,name = 'plants'),
]