from django.contrib import admin
from django.urls import path, include
from base import views
urlpatterns = [
    path('',views.home, name="home"),
    path('products', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('order_form', views.order_form, name="order_form"),

]