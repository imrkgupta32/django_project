
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from capp.models import  Company



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'email_id', 'ph_no', 'state', 'city', 'zipcode')
 
 
 
 
 
 
 
 
 
 
# # Register your models here.
# from django.contrib import admin
# from django.contrib.auth.models import User
# from capp.models import  Company



# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'company', 'email_id', 'ph_no', 'state', 'city', 'zipcode')
 