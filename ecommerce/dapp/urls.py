from django.contrib import admin
from django.urls import path, include
from dapp import views

# app_name='dapp'

urlpatterns = [
    
    path('dealer-details/',views.dealer_detail),
   
]