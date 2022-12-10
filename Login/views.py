from django.shortcuts import render

templete = 'Login/index.html'
context = {}

def index(request):
    return render(request, templete, context)