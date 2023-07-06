from django.contrib import admin
from .models import   Product, Orders, OrderItem
# Register your models here.


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email_id', 'ph_no', 'state', 'city', 'zipcode')

# @admin.register(Dealer)
# class DealerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'company' )

# @admin.register(FieldStaff)
# class FieldStaffAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'ph_no', 'email_id', 'state', 'city', 'zipcode', 'experience_years', 'dealer', 'company')

# @admin.register(Retailer)
# class RetailerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email_id', 'ph_no', 'state', 'city', 'zipcode', 'fieldstaff', 'dealer',  'company')

@admin.register(Product)
class DealerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(company=request.user)
        return queryset
    list_display = ('id', 'name', 'description', 'price', 'image', 'company' )
    # list_editable =('price', )



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'price')



@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'retailer', 'fieldstaff', 'retailer', 'order_date', 'total_amount')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')