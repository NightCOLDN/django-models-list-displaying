# main/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем файл books/urls.py ко всем адресам, которые начинаются с books/
    path('books/', include('books.urls')),
]
