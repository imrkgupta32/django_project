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
    list_display = ('id', 'dealer', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'company' )
    search_fields = ('ph_no',)


        
        
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


        
