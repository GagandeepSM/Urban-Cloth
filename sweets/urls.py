from django.contrib import admin
from django.urls import path

from sweets import views

urlpatterns = [
    path('', views.index , name='sweets'),
    path('contact/', views.contact, name='contact' ),
    path('products/', views.products, name='products' ),
]
