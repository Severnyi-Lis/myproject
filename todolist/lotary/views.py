from django.shortcuts import render
import random
# Создать приложение со страницей-шаблоном.
# На странице должны быть заготовлены места под имя и отчество.
# Страница должна поздравлять человека с выигрышем в лотерее.
# Сумма выигрыша тоже должна передаваться на страницу.
# если 1000 000, написать "лимон"
# Если 1000, написать "тыща"
# В остальных случаях выводить сумму.

# 71 рубль

# 2,3,4 рубля

# 5... рублей и т.д.

# Сумму брать случайным образом
# Create your views here.
def wins(request):
    congrate = ''
    number = random.randint(1,1000000)
    if number == 1000000:
        congrate = ' Вы выиграли лимон!'
    elif number == 1000:
        congrate = 'Вы выиграли тыщу!'
    else:
        congrate = 'Вы выиграли',number,'руб.'
    return render(
        request,
        "lotary/wins.html",
        {
            'wins': congrate,
            'imia': 'Вера',
            'otchestvo':'Олеговна',
        }
    )