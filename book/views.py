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

def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Book Successfully Updated')
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {'form': form, 'object': book_object})

def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse("Book Deleted")