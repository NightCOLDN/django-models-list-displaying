# books/admin.py
from django.contrib import admin
from .models import Book

# Настраиваем отображение колонок и фильтров в панели администратора
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'pub_date')  # Колонки в таблице
    list_filter = ('pub_date', 'author')                 # Фильтры справа
    search_fields = ('name', 'author')                   # Поиск по названию и автору
