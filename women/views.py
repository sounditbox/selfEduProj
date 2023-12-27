import datetime

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('Страница приложения women.')


def categories(request: HttpRequest, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>ID: {cat_id}')


def categories_by_slug(request: HttpRequest, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>Slug: {cat_slug}')


def archive(request: HttpRequest, year):
    if year > datetime.datetime.now().year:
        raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>Год: {year}')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')