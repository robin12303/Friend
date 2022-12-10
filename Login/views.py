from django.shortcuts import render
from django.http import HttpResponse

template = 'Login/bootstrap.html'
context = {}

def logined(request):
    return render(request , template, context)

def index(request):
    return render(request, template, context)