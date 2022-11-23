from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

template = 'BillPayment/bill.html'
context = {}

def index(request):
    return render(request, template, context)
