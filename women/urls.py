from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

    path('template_filters_cheatsheet/', views.template_filters_cheatsheet, name='template_filters_cheatsheet'),

    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),

    # re_path(r'^archive/(?P<year>[0-9]{4})', views.archive) => converters.py
    path('archive/<year4:year>', views.archive, name='archive'),
]

