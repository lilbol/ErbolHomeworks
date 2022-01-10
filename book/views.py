from django.shortcuts import render
from . import models

def book_all(requests):
    book = models.Book.objects.all()
    return render(requests, 'book_list.html', {'book': book})
