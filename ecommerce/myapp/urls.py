from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


# app_name='myapp'

urlpatterns = [
    # path('search/', views.search_products, name='search_products'),
    path('product-details/<int:product_id>',views.product_detail),
    path('orders-details/',views.order_detail),
    path('order-item-details/',views.order_item_detail),
]
