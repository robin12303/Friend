from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

context = {
    'islogin' : True,
}
urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name = 'Login/index.html'), name='login_index'),
    path('logout', auth_views.LogoutView.as_view(), name='login_logout')
]