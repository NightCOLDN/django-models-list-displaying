# books/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    # Если адрес пустой (в рамках приложения, то есть просто /books/), вызываем books_list
    path('', views.books_list, name='books_list'),

    # Если адрес содержит дату в формате YYYY-MM-DD (например, /books/2021-05-05/)
    # Используем регулярное выражение: \d{4} — 4 цифры года, \d{2} — две цифры месяца и дня
    re_path(r'^(?P<pub_date>\d{4}-\d{2}-\d{2})/$', views.books_by_date, name='books_by_date'),
]
