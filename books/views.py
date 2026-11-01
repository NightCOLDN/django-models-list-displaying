# books/views.py
from django.shortcuts import render
from .models import Book
import datetime

def books_list(request):
    """Страница со всеми книгами"""
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)

def books_by_date(request, pub_date):
    """Страница книг за конкретную дату с пагинацией"""
    template = 'books/books_by_date.html'

    # 1. Извлекаем книги за переданную в URL дату
    books = Book.objects.filter(pub_date=pub_date)

    # 2. Ищем в базе данных БЛИЖАЙШУЮ предыдущую дату
    prev_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()

    prev_date = prev_book.pub_date.strftime('%Y-%m-%d') if prev_book else None

    # 3. Ищем в базе данных БЛИЖАЙШУЮ следующую дату
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    next_date = next_book.pub_date.strftime('%Y-%m-%d') if next_book else None


    context = {
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)
