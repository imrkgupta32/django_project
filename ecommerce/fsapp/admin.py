
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FieldStaff
from .models import Dealer
from .models import Company

@admin.register(FieldStaff)
class FieldStaffAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if not request.user.is_superuser and hasattr(request.user, 'dealer'):
            dealer = request.user.dealer
            queryset = queryset.filter(dealer=dealer)
        
        
        elif request.user.groups.filter(name='Group_Dealer').exists():
            queryset = queryset.filter(dealer=Dealer.objects.get(dealer=request.user))
        
        
        
        elif request.user.groups.filter(name='Group_company').exists():
            company = Company.objects.get(company=request.user).company
            queryset = queryset.filter(company=company)    
            
           
        return queryset
    
    
    list_display = ('id','email_id', 'fieldstaff',  'phone_no', 'experience_years', 'address', 'nationality', 'state', 'city', 'zipcode', 'dealer', 'company')
    search_fields = ('id','email_id', 'fieldstaff',  'phone_no', 'experience_years', 'address', 'nationality', 'state', 'city', 'zipcode', 'dealer', 'company')
    list_filter = ('phone_no', 'address', 'state', 'city')

















# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import FieldStaff
# from .models import Dealer
# from .models import Company

# @admin.register(FieldStaff)
# class FieldStaffAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
        
#         if not request.user.is_superuser and hasattr(request.user, 'dealer'):
#             dealer = request.user.dealer
#             queryset = queryset.filter(dealer=dealer)
        
        
#         elif request.user.groups.filter(name='Group_Dealer').exists():
#             queryset = queryset.filter(dealer=Dealer.objects.get(dealer=request.user))
        
        
        
#         elif request.user.groups.filter(name='Group_company').exists():
#             company = Company.objects.get(company=request.user).company
#             queryset = queryset.filter(company=company)    
            
        
            
#         return queryset
    
    
#     list_display = ('id', 'fieldstaff', 'email_id', 'ph_no', 'state', 'city', 'zipcode', 'experience_years', 'dealer', 'company')


