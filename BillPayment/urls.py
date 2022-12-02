from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='billpayment_index'),
    path('detail', views.detail, name='billpayment_detail'),
    path('pay', views.pay, name='billpayment_pay'),
    path('bill', views.bill, name='billpayment_bill'),
    path('receipt', views.receipt, name='billpayment_receipt'),
]