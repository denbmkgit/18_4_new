from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_main_page(request):
    title = 'Главная страница'
    games = 'Игры'
    list = ['Atomic Heart', 'Cyberpunk', 'PayDay']
    context = {
        'title': title, 'games': games, 'list': list,
    }
    return render(request, 'main_page.html', context)


def page_games(request):
    list = ['Atomic Heart', 'Cyberpunk', 'PayDay']
    context = {
        'list': list,
    }
    return render(request, 'first_dop_page.html', context)

def basket(request):
    return render(request, 'second_dop_page.html')

