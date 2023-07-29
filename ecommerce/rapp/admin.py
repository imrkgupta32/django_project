from django.urls import reverse
from django.utils.html import format_html
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
            
    list_display = ('id','first_name', 'last_name', 'email_id', 'retailer', 'phone_number','address', 'nationality', 'state', 'city', 'zipcode',  'fieldstaff', 'dealer', 'company', 'loyalty_points',)
    exclude=('fieldstaff', 'dealer', 'company', )
    search_fields = ('first_name', 'last_name','phone_number','address', 'nationality', 'state', 'city')
    list_filter = ('company', 'dealer', 'fieldstaff', 'state',)

    def save_model(self, request, obj, form, change):
        print(request.user.fieldstaff_profile.all())
        if not obj.fieldstaff:
            obj.fieldstaff = request.user.fieldstaff_profile.all()[0]
            obj.dealer = request.user.fieldstaff_profile.all()[0].dealer
            obj.company = request.user.fieldstaff_profile.all()[0].company
        obj.save()


    def orders_summary(self, obj):
        aggregated_orders = obj.get_aggregated_orders()
        summary = ""
        for order in aggregated_orders:
            summary += f"Order ID: {order['order__id']}, Date: {order['order__order_date']}, Total Amount: {order['total_amount']}, Total Quantity: {order['total_quantity']}\n"
        return summary

    orders_summary.short_description = "Orders Summary"


    def view_loyalty_points(self, obj):
        url = reverse('view_loyalty_points')
        return format_html('<a href="{}">View Loyalty Points</a>', url)
    view_loyalty_points.short_description = 'Loyalty Points'

