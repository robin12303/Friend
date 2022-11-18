from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

template = 'Main/index.html'
context = {
    'islogin' : True,
    'id' : "adsf",
    'pw' : "asdf",
    'user_name': 'adsf',
}

def logout(request):
    context
    if request.method == 'POST':
        context["islogin"] = False
    return render(request, template, context)

def index(request):
    context
    return render(request,template, context)