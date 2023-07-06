from django.contrib import admin
from django.urls import path, include
from myapp import views

# app_name='myapp'

urlpatterns = [
    
    path('product-details/',views.product_detail),
    path('orders-details/',views.order_detail),
    path('order-item-details/',views.order_item_detail),
   
]