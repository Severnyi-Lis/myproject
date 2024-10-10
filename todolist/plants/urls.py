from django.urls import path
#from .views import unpretentious_plants,rastenie_main_page,sort_of_plants,about_us,contacts,korzina,office_plant,room_plant,information,otzivy
from . import views 
urlpatterns = [
    path('layout',views.layout,name = 'layout'),
    path('about_us/',views.about_us,name = 'about_us'),
    path('contacts/',views.contacts, name = 'contacts'),
    path('korzina/',views.korzina,name = 'korzina'),
    path('office_plant/',views.office_plant,name = 'office_plant'),
    path('room_plant/', views.room_plant,name = 'room_plant'),
    path('unpretentios_plant/',views.unpretentious_plant,name = 'unpretentious_plant'),
    path('information/',views.information,name = 'information'),
    path('otzivy/',views.otzivy,name = 'otzivy'),
    path('blog/',views.blog,name = 'blog'),
    path('dostavka_oplata/',views.dostavka,name = 'dostavka_oplata'),
    path('sovets/',views.sovets,name = 'sovets'),
    path('ask_and_answer/',views.ask_and_answer,name = 'ask_and_answer'),
    path('stocks/',views.stocks,name = 'stocks'),
    path('stocks_15/',views.stocks_15,name = 'stocks_15'),
    path('opt/',views.opt,name = 'opt'),
    path('exzotic/',views.exzotic,name = 'exzotic'),
    path('zakaz/',views.zakaz,name = 'zakaz'),
    path('register/', views.register, name='register'),
    path('/',views.index,name = 'index'),
]