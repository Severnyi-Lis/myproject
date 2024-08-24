from django.shortcuts import render

# Create your views here.
def plants(request):
    context = {}
    return render(
        request,
        "plants/rastenie.html",
        context
    )
