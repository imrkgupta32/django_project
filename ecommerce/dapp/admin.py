from django.contrib import admin
from dapp.models import   Dealer
from capp.models import   Company
from fsapp.models import   FieldStaff
from django.contrib.auth.models import User


# # Register your models here.
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Set the company field to the logged-in company
        obj.company = request.user
        obj.save()
        
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.groups.filter(name='Group_FieldStaff').exists():
            company = FieldStaff.objects.get(fieldstaff=request.user).company
            queryset = queryset.filter(company=company)
            
        if request.user.groups.filter(name='Group_Dealer').exists():
            company = Dealer.objects.get(dealer=request.user).company
            queryset = queryset.filter(company=company)

        if request.user.groups.filter(name='Group_company').exists():
            company = Company.objects.get(company=request.user).company
            queryset = queryset.filter(company=company)
                
            
        return queryset
    list_display = ('id', 'dealer', 'first_name', 'last_name', 'email_id', 'phone_number',  'address', 'nationality', 'state', 'city', 'zipcode', 'company')
    exclude=('company',)      
    search_fields = ('first_name', 'last_name', 'phone_number',  'address', 'nationality', 'state', 'city')
    list_filter = ('company', 'state', )

        
        

        
