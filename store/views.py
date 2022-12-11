from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Operator, Resident


def index(request):
    """
    Operator Lists
    """
    oper_list = Operator.objects.order_by('oper_id')
    context = {'oper_list': oper_list}
    return render(request, 'store/oper_list.html', context)


def detail(request, oper_list):
    """
    oper detail
    """
    op = Operator.objects.get(oper_id=oper_list)
    context = {'op': op}
    return render(request, 'store/oper_detail.html', context)

def resident_index(request):
    """
    resident_index Lists
    """
    res_list = Operator.objects.order_by('id')
    context = {'oper_list': res_list}
    return render(request, 'store/oper_list.html', context)


def resident_detail(request, oper_list):
    """
    resident_detail detail
    """
    res = Resident.objects.get(id=oper_list)
    context = {'op': res}
    return render(request, 'store/oper_detail.html', context)