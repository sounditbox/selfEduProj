import datetime

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request: HttpRequest):
    return render(request, 'women/index.html')


def about(request: HttpRequest):
    return render(request, 'women/about.html')


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
