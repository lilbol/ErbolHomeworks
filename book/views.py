from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def book_all(requests):
    book = models.Book.objects.all()
    return render(requests, 'book_list.html', {'book': book})


def book_detail(requests, id):
    books = get_object_or_404(models.Book, id=id)
    return render(requests, 'book_detail.html', {'books': books})

def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_books.html', {'form': form})