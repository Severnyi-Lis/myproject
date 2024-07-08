from django.urls import path
from .views import wins
urlpatterns = [
    path('', wins,name = 'wins'),
]