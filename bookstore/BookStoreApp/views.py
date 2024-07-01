from django.shortcuts import render, get_object_or_404
from .models import Book
def index(request):

    queryset = Book.objects.filter().all()
    context = {'books' : queryset}

    return render(request, 'index.html', context = context)


def book_detail(request, id):
    return render(request, 'book_detail.html', context={'book': Book.objects.get(id=id)})