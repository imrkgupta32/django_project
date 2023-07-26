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
            
    list_display = ('id','email_id', 'retailer', 'phone_number','address', 'nationality', 'state', 'city', 'zipcode', 'fieldstaff', 'dealer', 'company')
    exclude=('fieldstaff', 'dealer', 'company',)
    search_fields = ('email_id','phone_number','address', 'nationality', 'state', 'city')
    list_filter = ('phone_number','address', 'state', 'city',)

    def save_model(self, request, obj, form, change):
        print(request.user.fieldstaff_profile.all())
        if not obj.fieldstaff:
            obj.fieldstaff = request.user.fieldstaff_profile.all()[0]
            obj.dealer = request.user.fieldstaff_profile.all()[0].dealer
            obj.company = request.user.fieldstaff_profile.all()[0].company
        obj.save()




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







