from django.shortcuts import render
from .models import Rastenie


# Create your views here.
def layout(request):
    context = {}
    return render(
        request,
        "plants/layout.html",
        context
    )


def about_us(request):
    context = {}
    return render(
        request,
        "plants/about_us.html",
        context
    )


def contacts(request):
    context = {}
    return render(
        request,
        "plants/contacts.html",
        context
    )


def korzina(request):
    context = {}
    return render(
        request,
        "plants/korzina.html",
        context
    )


def office_plant(request):
    context = {}
    return render(
        request,
        "plants/office_plant.html",
        context
    )


def room_plant(request):
    context = {}
    return render(
        request,
        "plants/room_plant.html",
        context
    )


def unpretentious_plant(request):
    context = {}
    return render(
        request,
        "plants/unpretentious_plant.html",
        context
    )


def information(request):
    context = {}
    return render(
        request,
        "plants/information.html",
        context
    )


def otzivy(request):
    context = {}
    return render(
        request,
        "plants/otzivy.html",
        context
    )


def blog(request):
    context = {}
    return render(
        request,
        "plants/blog.html",
        context
    )


def dostavka(request):
    stoimost = 'Доставка по Москве - 590 ₽'
    night    = 'Доставка в вечернее время - 790 ₽'
    mo       = 'Доставка по МО 590 ₽ + 45 р/1 км'
    context = {
        'dostavochka': stoimost,
        'noch':        night,
        'oblast':      mo,
    }
    return render(
        request,
        "plants/dostavka_oplata.html",
        context
    )

def sovets(request):
    context = {}
    return render(
        request,
        "plants/sovets.html",
        context
    )


def ask_and_answer(request):
    context = {}
    return render(
        request,
        "plants/ask_and_answer.html",
        context
    )


def index(request):
    context = {}
    return render(
        request,
        "plants/index.html",
        context
    )


