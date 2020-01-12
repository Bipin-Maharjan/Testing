from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.loadBook,name='premiumbook'),
  path('description/<id>/',views.bookDescription,name='description'),
  path('addbook/',views.addBook,name='addbook'),
]