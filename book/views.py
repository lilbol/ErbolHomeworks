from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class BooksListView(generic.ListView):
    template_name = 'book_list.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.filter().order_by('-id')

# def book_all(requests):
#     book = models.Book.objects.all()
#     return render(requests, 'book_list.html', {'book': book})

class BooksDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id= book_id)
# def book_detail(requests, id):
#     books = get_object_or_404(models.Book, id=id)
#     return render(requests, 'book_detail.html', {'books': books})

class BooksCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/books/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)


# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book created')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_books.html', {'form': form})


class BooksUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)

    def form_valid(self, form):
        return super(BooksUpdateView, self).form_valid(form=form)


# def book_update(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book Successfully Updated')
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'book_update.html', {'form': form, 'object': book_object})


class BooksDeleteView(generic.DeleteView):
    template_name = 'confirm_delete_book.html'
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)
# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return HttpResponse("Book Deleted")
