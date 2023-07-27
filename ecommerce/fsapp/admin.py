
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
    
    
    list_display = ('id','email_id', 'first_name', 'last_name', 'fieldstaff',  'phone_number', 'address', 'nationality', 'state', 'city', 'zipcode', 'dealer', 'company')
    exclude=('dealer', 'company',)
    search_fields = ( 'phone_number', 'address', 'nationality', 'state', 'city')
    list_filter = ('company', 'dealer', 'state', 'city')

    def save_model(self, request, obj, form, change):
        print(request.user.dealer_profile.all())
        if not obj.dealer:
            obj.dealer = request.user.dealer_profile.all()[0]
            obj.company = request.user.dealer_profile.all()[0].company
        obj.save()
















