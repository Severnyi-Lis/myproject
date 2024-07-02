from django.urls import path
from .views import index,new_task,new_cat,menu,partners,index_2
urlpatterns = [
    path('', index,name = 'index'),
    path('newtask/',new_task, name='new_task'),
    path('cats/',new_cat, name='new_cat'),
    path('menu/',menu, name='menu'),
    path('partners/',partners,name='partners'),
    path('index_2/',index_2,name='index_2')
]