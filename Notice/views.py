from django.shortcuts import render

context = {
    'islogin' : True,
}

def index(request):
    template = 'Notice/index.html'
    return render(request, template, context)