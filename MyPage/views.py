from django.shortcuts import render

context = {}

def index(request):
    template = 'MyPage/index.html'
    return render(context, request, context)