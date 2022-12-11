from django.shortcuts import render

context = {
    'islogin' : True,
}

def bill(request):
    template = 'BillPayment/bill.html'
    return render(request, template, context)

def detail(request):
    template = 'BillPayment/detail.html'
    '''추후 변경 예정, 임시값'''
    detailcontext = {
        'data' : [
            ['data1',1],
            ['data2',1],
            ['data3',1],
            ['data4',1],
            ['data5',1],
            ['data6',1],
            ['data7',1],
            ['data8',1],
            ['data9',1],
            ['data10',1],
        ],
        'datatotal' : '1234'
    }
    detailcontext.update(context)
    return render(request, template, detailcontext)

def pay(request):
    template = 'BillPayment/pay.html'
    return render(request, template, context)

def index(request):
    template = 'BillPayment/index.html'
    return render(request, template, context)
