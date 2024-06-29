from django.shortcuts import render
from .models import Suplement, UploadImage, Category

# Create your views here.


def index(request):
    queryset = Suplement.objects.filter().all()
    context = {'suplements': queryset}
    return render(request,'index.html', context = context)

def picture(request):
    queryset = UploadImage.objects.filter().all()
    context = {'pictures': queryset}
    return render(request,'index.html', context = context)