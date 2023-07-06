from django.contrib import admin
from django.urls import path, include
from rapp import views
urlpatterns = [
    
    path('company-details/',views.retailer_detail),
   
]