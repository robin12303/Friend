from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login_index'),
    path('', views.logined, name = 'login_logined'),
]