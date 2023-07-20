from django.contrib import admin
from dapp.models import   Dealer
from django.contrib.auth.models import User


# # Register your models here.
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(company=request.user)
            
        return queryset
    list_display = ('id', 'dealer', 'email_id', 'phone_no', 'experience_years', 'address', 'nationality', 'state', 'city', 'zipcode', 'company')
    search_fields = ('id', 'dealer', 'email_id', 'phone_no', 'experience_years', 'address', 'nationality', 'state', 'city', 'zipcode', 'company')
    list_filter = ('email_id', 'phone_no', 'address', 'state', 'city',)

        
        
# from django.contrib import admin
# from dapp.models import   Dealer
# from django.contrib.auth.models import User


# # # Register your models here.
# @admin.register(Dealer)
# class DealerAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:
#             queryset = queryset.filter(company=request.user)
            
#         return queryset
#     list_display = ('id', 'dealer', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'company' )
#     search_fields = ('ph_no',)


        
