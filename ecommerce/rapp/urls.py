from django.contrib import admin
from django.urls import path, include
from rapp import views
urlpatterns = [
    
    # path('company-details/',views.retailer_detail),
    path('loyalty_points/', views.view_loyalty_points, name='view_loyalty_points'),
]
   
