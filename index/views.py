from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    queries = House.objects.all()
    context = {'queries': queries}
    return render(request, 'index/index.html', context)


def details(request, pk):
    queries = House.objects.get(id=pk)
    context = {'queries': queries}
    return render(request, 'index/detail2.html', context)
