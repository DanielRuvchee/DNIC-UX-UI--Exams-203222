from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def ask_events(request):
    return(request, 'ask_events.html')