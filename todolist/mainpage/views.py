# Create your views here.

from django.shortcuts import render
from datetime import datetime,timedelta
def index(request):
    plan = "хз когда"
    workplan = datetime(2024,5,28)
    worktoday = datetime.now()
    worktoday = datetime(
        worktoday.year,
        worktoday.month,
        worktoday.day,
    )
    if worktoday == workplan:
        plan = "сегодня"
    elif worktoday == workplan + timedelta(1):
        plan = 'завтра'
    elif worktoday == workplan - timedelta(1):
        plan = 'вчера' 

    return render(
         request,                    # Запрос
        'mainpage/index.html',      # путь к шаблону
          {
            'kogda':plan, #datetime.now(), #.strftime('%Y %B %d')
            'tasks': [ # Они будут получены из базы данных, а не вбиты в код вручную!
                {
                    'description': 'Записать два видео по Django', 
                    'done': True,
                },
                {
                    'description': 'Провести урок', 
                    'done': True,
                },
                {
                    'description': 'Пробежать 5 километров', 
                    'done': False,
                },
            ],
        }
    )                   
from .forms import TaskForm

def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': TaskForm(),
    }
    return render(
        request,                  # Запрос
	    'mainpage/newtask.html',  # путь к шаблону
        context                   # подстановки
    )

from .models import Cat
def new_cat(request):
    cats = Cat.objects.all()
    context = {
        "kogda":'Карточка котенка',
        "cats":cats,
    }
    return render(
        request,
        'mainpage/cats.html',
        context
    )
def menu(request):
    context = {}
    return render(
        request,
        "mainpage/menu.html",
        context
    )
def partners(request):
    context = {}
    return render(
        request,
        "mainpage/partners.html",
        context
    )
def index_2(request):
    context = {}
    return render(
        request,
        "mainpage/index_2.html",
        context
    )  