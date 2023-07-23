from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Retailer
from .models import Dealer
from .models import Company
from .models import FieldStaff
# Register your models here.
@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        print(request.user.groups.filter(name='Group_FieldStaff').exists())
        if not request.user.is_superuser:
            
            pass
        
        if request.user.groups.filter(name='Group_FieldStaff').exists():
            queryset = queryset.filter(fieldstaff=FieldStaff.objects.get(fieldstaff=request.user))
        
        elif request.user.groups.filter(name='Group_Dealer').exists():
            queryset = queryset.filter(dealer=Dealer.objects.get(dealer=request.user))
        
        
        
        elif request.user.groups.filter(name='Group_company').exists():
            company = Company.objects.get(company=request.user).company
            queryset = queryset.filter(company=company)    
            
        
            
        return queryset
            
    list_display = ('id','email_id', 'retailer', 'phone_no','address', 'nationality', 'state', 'city', 'zipcode', 'fieldstaff', 'dealer', 'company')
    search_fields = ('email_id','phone_no','address', 'nationality', 'state', 'city')
    list_filter = ('phone_no', 'address', 'state', 'city')





# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import Retailer
# from .models import Dealer
# from .models import Company
# from .models import FieldStaff
# # Register your models here.
# @admin.register(Retailer)
# class RetailerAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         print(request.user.groups.filter(name='Group_FieldStaff').exists())
#         if not request.user.is_superuser:
            
#             pass
        
#         if request.user.groups.filter(name='Group_FieldStaff').exists():
#             queryset = queryset.filter(fieldstaff=FieldStaff.objects.get(fieldstaff=request.user))
        
#         elif request.user.groups.filter(name='Group_Dealer').exists():
#             queryset = queryset.filter(dealer=Dealer.objects.get(dealer=request.user))
        
        
        
#         elif request.user.groups.filter(name='Group_company').exists():
#             company = Company.objects.get(company=request.user).company
#             queryset = queryset.filter(company=company)    
            
        
            
#         return queryset
            
#     list_display = ('id', 'retailer', 'email_id', 'ph_no','state', 'city', 'zipcode', 'fieldstaff', 'dealer', 'company' )







