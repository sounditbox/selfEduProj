from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('Страница приложения women.')


def categories(request: HttpRequest, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>ID: {cat_id}')


def categories_by_slug(request: HttpRequest, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>Slug: {cat_slug}')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>Год: {year}')
