from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Operator

def index(request):
    """
    operator
    """
    oper_list = Operator.objects.order_by('oper_id')
    context = {'oper_list': oper_list}
    return render(request, 'store/oper_list.html', context)
