from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
def index(request):

    queryset = Book.objects.filter().all()
    context = {'books' : queryset}

    return render(request, 'index.html', context = context)


def book_detail(request, id):
    return render(request, 'book_detail.html', context={'book': Book.objects.get(id=id)})

def add_book(request):
    queryset = Book.objects.filter(author=request.user).all()
    context = {'books': queryset, 'form': BookForm}
    return render(request, 'add_book.html', context = context)