
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from capp.models import  Company



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'email_id', 'phone_no', 'address', 'nationality', 'state', 'city', 'zipcode')
    search_fields = ('id', 'company', 'email_id', 'phone_no', 'address', 'nationality', 'state', 'city', 'zipcode')
    list_filter= ('address', 'email_id', 'phone_no', 'state', 'city' )
 
 
 
 

 
 
# # Register your models here.
# from django.contrib import admin
# from django.contrib.auth.models import User
# from capp.models import  Company



# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'company', 'email_id', 'ph_no', 'state', 'city', 'zipcode')
 