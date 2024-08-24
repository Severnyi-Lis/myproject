from django.shortcuts import render

# Create your views here.
def psich(request):
    context = {}
    return render(
        request,
        "psich/zapis.html",
        context
    )