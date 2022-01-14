from django.shortcuts import render, get_object_or_404
from . import models

def book_all(requests):
    book = models.Book.objects.all()
    return render(requests, 'book_list.html', {'book': book})


def book_detail(requests, id):
    books = get_object_or_404(models.Book, id=id)
    return render(requests, 'book_detail.html', {'books': books})