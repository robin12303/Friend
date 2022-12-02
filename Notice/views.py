from django.shortcuts import render

context = {
    'islogin' : True,
}

def notice(request):
    template = 'Notice/notice.html'
    return render(request, template, context)

def inquiry(request):
    template = 'Notice/inquiry.html'
    return render(request, template, context)

def index(request):
    template = 'Notice/index.html'
    return render(request, template, context)