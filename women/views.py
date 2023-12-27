import datetime

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request: HttpRequest):
    return render(request, 'women/index.html', {'title': 'Главная страница'})


def template_filters_cheatsheet(request):
    class MyClass:
        def __init__(self, a, b):
            self.a, self.b = a, b

    menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
    context = {
        'title': 'примеры использования фильтров в шаблонах',
        'menu': menu,
        'float': 42.1,
        'lst': [1, 2, 3],
        'set': {4, 5, 6},
        'dict': {'key': 'value', 'key2': 42},
        'object': MyClass(1, 2),
    }
    return render(request, 'women/template_filters_cheatsheet.html', context)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request: HttpRequest, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>ID: {cat_id}')


def categories_by_slug(request: HttpRequest, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>Slug: {cat_slug}')


def archive(request: HttpRequest, year):
    if year > datetime.datetime.now().year:
        return redirect(reverse('cats', args=('music',)))
    return HttpResponse(f'<h1>Архив по годам</h1><p>Год: {year}')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
