from django.shortcuts import render
from django.http import HttpResponse

templet = 'Login/bootstrap.html'

def index(request):
    return render(request, templet)