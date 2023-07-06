from django.contrib import admin
from .models import Retailer
# Register your models here.
@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    # class FieldStaffAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(company=request.user)
        
        return queryset
    list_display = ('id', 'email_id', 'ph_no','state', 'city', 'zipcode', 'fieldstaff', 'dealer', 'company' )
