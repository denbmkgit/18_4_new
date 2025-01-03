from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_main_page(request):
    title = 'Главная страница'
    games = 'Игры'
    context = {
        'title': title, 'games': games
    }
    return render(request, 'main_page.html', context)

class page_games(TemplateView):
    template_name = 'first_dop_page.html'

