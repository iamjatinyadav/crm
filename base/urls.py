from django.contrib import admin
from django.urls import path, include
from base import views
urlpatterns = [
    path('',views.home, name="home"),
    path('products', views.products, name="products"),
    path('customer', views.customer, name="customer"),

]