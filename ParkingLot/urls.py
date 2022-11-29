from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='parkinglot_index'),
    path('logout', views.logout, name='parkinglot_logout'),
    path('resident', views.resident, name='parkinglot_resident'),
    path('guest', views.guest, name='parkinglot_guest'),
    path('input', views.input, name='parkinglot_input'),
]