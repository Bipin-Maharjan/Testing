from django.urls import path
from . import views
 
urlpatterns = [
	#path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('loginForm/', views.loginForm, name='loginForm'),
    path('register/', views.register, name='register'),
    path('registerForm/', views.registerForm, name='registerForm'),
]

 