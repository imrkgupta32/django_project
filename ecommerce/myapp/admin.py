from django.contrib import admin
from .models import   Product, Orders, OrderItem
# Register your models here.


from fsapp.models import FieldStaff
from dapp.models import Dealer
from capp.models import Company
from rapp.models import Retailer
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db.models import Q
from itertools import chain

class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        
        # Retrieve the default queryset
        queryset = super().get_queryset(request)
        
        # Apply your custom query here
        # For example, filter users with a specific condition
        ids = [request.user.id,]
        if request.user.groups.filter(name='Group_Dealer').exists():
            queryset1 = FieldStaff.objects.filter(dealer = Dealer.objects.get(dealer=request.user))
            for i in queryset1:
                ids.append(i.fieldstaff.id)
            queryset2 = Retailer.objects.filter(dealer = Dealer.objects.get(dealer=request.user))
            for i in queryset2:
                ids.append(i.retailer.id)
            print(ids)
            queryset = queryset.filter(Q(pk__in=ids))
            
        elif request.user.groups.filter(name='Group_company').exists():
            queryset3 = Dealer.objects.filter(company=request.user)
            for i in queryset3:
                ids.append(i.dealer.id)
            queryset1 = FieldStaff.objects.filter(company=request.user)
            for i in queryset1:
                ids.append(i.fieldstaff.id)
            queryset2 = Retailer.objects.filter(company=request.user)
            for i in queryset2:
                ids.append(i.retailer.id)
            queryset = queryset.filter(Q(pk__in=ids))
            
        elif request.user.groups.filter(name='Group_FieldStaff').exists():
            queryset2 = Retailer.objects.filter(fieldstaff=FieldStaff.objects.get(fieldstaff=request.user))
            for i in queryset2:
                ids.append(i.retailer.id)
            queryset = queryset.filter(Q(pk__in=ids))
        else:
            pass
        
        print(queryset)
        
        return queryset


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


from django.contrib.auth.admin import UserAdmin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    
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
    

    def save_model(self, request, obj, form, change):
        # Update the location_status based on the status if needed
        if obj.status == 'd':  # If the status is 'Delivered'
            obj.location_status = 'd'  # Set location_status to 'Delivered'
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        # Make the location_status field readonly for certain conditions
        if obj and obj.status == 'd':
            return ('location_status',)
        return super().get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Disable delete action for products with 'Delivered' status
        if obj and obj.status == 'd':
            return False
        return super().has_delete_permission(request, obj)   
   
   
   
    list_display = ('id', 'name', 'main_category', 'sub_category', 'description', 'price', 'image', 'status', 'location_status', 'company',)
    exclude=('company',)
    list_filter = ( 'status', 'location_status')
    search_fields = ( 'name', 'description', 'price' )
    
    
    def save_model(self, request, obj, form, change):
        # Set the company field to the logged-in user (company user) creating the product
        if not obj.company:
            obj.company = request.user
        super().save_model(request, obj, form, change)
    
    
    

from myapp.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
       
    list_display = ('id',  'name')
    list_filter= ('name', )
    search_fields = ('name',)
    

from .models import Review    
from .models import Rating    

# Register the Review model in the admin site
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'retailer', 'product', 'created_at' , 'text')
    exclude=('retailer',)
    list_filter = ('created_at',)
    search_fields = ('retailer__username', 'product__name')
    
    def save_model(self, request, obj, form, change):
        
        if not obj.retailer:
            obj.retailer = request.user
        super().save_model(request, obj, form, change)


# Register the Rating model in the admin site
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'product', 'rating')
    exclude=('retailer',)
    list_filter = ('rating',)
    search_fields = ('retailer__username', 'product__name')
    
    def save_model(self, request, obj, form, change):
        
        if not obj.retailer:
            obj.retailer = request.user
        super().save_model(request, obj, form, change)



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

# from django.utils.html import format_html
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F, DecimalField,  Case, When
from django.db.models.functions import Coalesce
from decimal import Decimal
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        user = request.user
        
        if user.groups.filter(name='Group_Retailer').exists():
            retails = Retailer.objects.get(retailer=user)
            queryset = queryset.filter(retailer__company=retails.company)
     
        if user.groups.filter(name='Group_FieldStaff').exists():
            field_staff = FieldStaff.objects.get(fieldstaff=user)
            queryset = queryset.filter(retailer__company=field_staff.company)    
        
        if user.groups.filter(name='Group_Dealer').exists():
            dealer = Dealer.objects.get(dealer=user)
            queryset = queryset.filter(dealer__company=dealer.company)    
        
        if request.user.groups.filter(name='Group_company').exists():
            company = Company.objects.get(company=request.user).company
            # Filter the queryset to include orders related to the company
            queryset = queryset.filter(dealer__company=company)

        return queryset
    
    list_display = ('id', 'product', 'price', 'order_date', 'status', 'order_location', 'retailer', 'fieldstaff', 'dealer', 'company', 'total_purchase',)
    exclude=('retailer', 'fieldstaff', 'dealer', 'company', 'price', 'total_purchase',)
    list_filter = ('order_date',)
    inlines = [OrderItemInline]
    # search_fields = ( 'product', 'retailer', 'fieldstaff', 'dealer', 'order_date')
    
    def total_purchase(self, obj):
        return obj.total_purchase

    total_purchase.short_description = 'Total Purchase'
    total_purchase.admin_order_field = 'total_purchase'


    
        
    def save_model(self, request, obj, form, change):
        print(request.user.retailer_profile.all())
        if not obj.retailer:
            obj.price = obj.product.price if obj.product else Decimal('0.00')
            obj.retailer = request.user.retailer_profile.all()[0]
            obj.fieldstaff = request.user.retailer_profile.all()[0].fieldstaff
            obj.dealer = request.user.retailer_profile.all()[0].dealer
            obj.company = request.user.retailer_profile.all()[0].company
        obj.save()
        
        super().save_model(request, obj, form, change)

        # Calculate the total_purchased based on the sum of total_amounts of associated OrderItems
        total_purchase = form.instance.orderitem_set.aggregate(total_purchase=Sum('total_amount'))['total_purchase']
        form.instance.total_purchase = total_purchase if total_purchase is not None else 0.0
        form.instance.save()
        
    
        
from django.db.models import Count

orders = Orders.objects.values_list('retailer', 'product', 'price').annotate(total_orders=Count('id'))
    
    
from django.contrib import messages
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if request.user.groups.filter(name='Group_Retailer').exists():
            retailer = Retailer.objects.get(retailer=request.user)
            queryset = queryset.filter(order__retailer=retailer)
        
        if request.user.groups.filter(name='Group_FieldStaff').exists():
            fieldstaff = FieldStaff.objects.get(fieldstaff=request.user)
            queryset = queryset.filter(order__fieldstaff=fieldstaff)

        if request.user.groups.filter(name='Group_Dealer').exists():
            dealer = Dealer.objects.get(dealer=request.user)
            queryset = queryset.filter(order__dealer=dealer)

        if request.user.groups.filter(name='Group_company').exists():
            company = Company.objects.get(company=request.user).company
            queryset = queryset.filter(order__dealer__company=company)

        return queryset

    
    list_display = ('order', 'retailer', 'quantity','product', 'total_amount',)
    exclude=('total_amount', 'retailer', 'loyalty_points',)
    list_filter = ( 'quantity', )
    # search_fields = ('quantity', )
    
    
    
    
    
    
    def save_model(self, request, obj, form, change):
        if not obj.retailer:
            try:
                retailer_profile = request.user.retailer_profile.first()
                if retailer_profile:
                    obj.retailer = retailer_profile
                else:
                    # Create a new Retailer instance if none exists
                    obj.retailer = Retailer.objects.create(name='New Retailer')
            except Retailer.DoesNotExist:
               
                pass
        
       
    # def save_model(self, request, obj, form, change):    
        if not obj.total_amount:
            # Retrieve the price of the associated product
            product_price = obj.product.price if obj.product else Decimal('0.00')
            # Calculate the total amount based on the quantity and product price
            obj.total_amount = product_price * obj.quantity

            # Calculate and update the loyalty points earned by the retailer
            loyalty_points_earned = int(obj.total_amount)  # 1 point for every Rs 1 spent
            obj.retailer.loyalty_points += loyalty_points_earned
            obj.retailer.save()
            
        super().save_model(request, obj, form, change)
    
    
    
from myapp.models import Cart
from myapp.models import CartItem
class CartAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if request.user.groups.filter(name='Group_Retailer').exists():
            retailer = request.user  # Assuming request.user is a User instance representing the logged-in retailer
            queryset = queryset.filter(retailer=retailer)
            
            

        return queryset
    
    
    
    
    
    list_display= ('id', 'product', 'retailer')
    exclude=('retailer',)
    list_filter= ('product', )
    search_fields= ('id', 'product')
    
    def save_model(self, request, obj, form, change):
        if not obj.retailer:
            obj.retailer = request.user
        super().save_model(request, obj, form, change)

    
    pass
    
admin.site.register(Cart, CartAdmin)        

class CartItemAdmin(admin.ModelAdmin):  
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if request.user.groups.filter(name='Group_Retailer').exists():
            retailer = request.user
            queryset = queryset.filter(cart__retailer=retailer)

        return queryset
    
    
    
    list_display= ('id', 'cart', 'product', 'quantity', 'price', 'retailer')
    exclude=('retailer','price',)
    list_filter= ('product', 'quantity')
    search_fields= ('id', 'product', 'quantity','cart')
    
    def save_model(self, request, obj, form, change):
        
        if not obj.retailer:
            obj.retailer = request.user
        super().save_model(request, obj, form, change)
        
    pass

admin.site.register(CartItem, CartItemAdmin)   




from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')
    list_filter = ('is_read',)
    search_fields = ( 'message',)  # Allows searching by username of the related user

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Restrict the queryset to show notifications of the current logged-in user
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs

admin.site.register(Notification, NotificationAdmin)    
    

