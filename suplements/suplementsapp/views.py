from django.shortcuts import render
from .models import Suplement, UploadImage, Category
from .forms import SuplementForm

# Create your views here.


def index(request):
    queryset = Suplement.objects.filter().all()
    context = {'suplements': queryset}
    return render(request,'index.html', context = context)

def picture(request):
    queryset = UploadImage.objects.filter().all()
    context = {'pictures': queryset}
    return render(request,'index.html', context = context)


def suplement_detail(request, id):
    return render(request, 'suplement_detail.html', context={'suplement': Suplement.objects.get(id=id)})


def add_new(request):
    context = {'form': SuplementForm}
    return render(request, 'addnew.html', context)