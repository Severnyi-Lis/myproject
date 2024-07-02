from django.urls import path
from .views import search_cat
urlpatterns = [
    path('', search_cat,name = 'kitty'),
]