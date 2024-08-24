from django.urls import path
from .views import psich
urlpatterns = [
    path('', psich,name = 'psich'),
]