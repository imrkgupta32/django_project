from django.contrib import admin
from django.urls import path, include
from capp import views

# app_name= 'capp'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about-us/',views.aboutUs),
    path('company-details/',views.company_detail, name= 'company_details'),
   
]