from django.shortcuts import render
from .models import Rastenie
from .forms import UserRegistrationForm  #, LoginForm 

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
    context = {}
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


def stocks(request):
    context = {}
    return render(
        request,
        "plants/stocks.html",
        context
    )


def stocks_15(request):
    context = {}
    return render(
        request,
        "plants/stocks_15.html",
        context
    )


def opt(request):
    context = {}
    return render(
        request,
        "plants/opt.html",
        context
    )


def exzotic(request):
    context = {}
    return render(
        request,
        "plants/exzotic.html",
        context
    )


def zakaz(request):
    context = {}
    return render(
        request,
        "plants/zakaz.html",
        context
    )

 
def register(request): 
    if request.method == 'POST': 
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid(): 
            # Create a new user object but avoid saving it yet 
            new_user = user_form.save(commit=False) 
            # Set the chosen password 
            new_user.set_password(user_form.cleaned_data['password']) 
            # Save the User object 
            new_user.save() 
            return render(request, 'plants/registration_pass.html', {'new_user': new_user}) 
    else: 
        user_form = UserRegistrationForm() 
    return render( 
        request, 
        'plants/registration.html', 
        { 
            'user_form': user_form 
        })

