from django.contrib import admin
from dapp.models import   Dealer
# # Register your models here.
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(company=request.user)
            
        return queryset
    list_display = ('id', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'company' )



# from django.contrib import admin
# from dapp.models import   Dealer
# # # Register your models here.
# @admin.register(Dealer)
# class DealerAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         # if not request.user.is_staff:
#             # Filter dealers based on the logged-in company
#         queryset = queryset.filter(company=request.user)
#         return queryset
#     list_display = ('id', 'name', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'company' )

