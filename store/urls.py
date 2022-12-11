from django.urls import path


from . import views

app_name = 'store'

urlpatterns =[
    path('', views.index, name='index'),
    path('<str:oper_list>/', views.detail),
]