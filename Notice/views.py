from django.shortcuts import render
from .models import *

context = {
    'inquiry' : InquiryBoard.objects.order_by('-b_number'),
    'notice' : Notice.objects.order_by('-ntc_number'),
}

def index(request):
    template = 'Notice/index.html'
    return render(request, template, context)