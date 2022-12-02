from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='notice_index'),
    path('notice', views.notice, name='notice_notice'),
    path('inquiry', views.inquiry, name='notice_inquiry'),
]