from django.contrib import admin
from django.urls import path, include
from fsapp import views

# app_name='fsapp'

urlpatterns = [
    
    path('company-details/',views.fieldstaff_detail),
   
]