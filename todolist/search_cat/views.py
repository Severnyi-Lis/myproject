from django.shortcuts import render

# Create your views here.

from .models import Kitten
def search_cat(request):
    if request.method == "POST":
#       form = KittenForm(request.POST, request.FILES)
        print(request.POST)
   #     print(request.POST['Catname'][0])
        print(request.POST.get('Catname'))
        context = {'kotenok':'котята убежали!' }
        kittens_found = Kitten.objects.filter(namecat=request.POST.get('Catname'))
        if kittens_found:
            context = {
                'kotenok': kittens_found,
            }
        else:
            print('проверка котенка',kittens_found)
        return render(
            request,                  # Запрос
          'search_cat/kotenok_render.html',  # путь к шаблону
            context                   # подстановки
        )

    context = { }
    return render(
        request,                  # Запрос
      'search_cat/kot.html',  # путь к шаблону
        context                   # подстановки
    )
