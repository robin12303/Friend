from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'BillPayment/관리비고지서.html')
