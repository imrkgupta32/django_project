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

from django.contrib import admin
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
   
   
   
    list_display = ('id', 'name', 'main_category', 'sub_category', 'description', 'price', 'image', 'status', )
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
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if request.user.groups.filter(name='Group_company').exists():
    #         company = Company.objects.get(company=request.user).company
    #         queryset = queryset.filter(company=company)
            
    #     return queryset    
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
    
    list_display = ('id', 'product',  'order_date', 'status','price', 'retailer', 'fieldstaff', 'dealer', 'company')
    exclude=('retailer', 'fieldstaff', 'dealer', 'company',)
    list_filter = ('order_date',)
    # search_fields = ( 'product', 'retailer', 'fieldstaff', 'dealer', 'order_date')
    
    def save_model(self, request, obj, form, change):
        print(request.user.retailer_profile.all())
        if not obj.retailer:
            obj.retailer = request.user.retailer_profile.all()[0]
            obj.fieldstaff = request.user.retailer_profile.all()[0].fieldstaff
            obj.dealer = request.user.retailer_profile.all()[0].dealer
            obj.company = request.user.retailer_profile.all()[0].company
        obj.save()

    
    

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

    list_display = ('order', 'quantity','product', 'total_amount' )
    list_filter = ( 'quantity', )
    # search_fields = ('quantity', )
    
       
from myapp.models import Cart
from myapp.models import CartItem
admin.site.register(Cart)
class CartAdmin(admin.ModelAdmin):
    
    list_display= ('id', 'product', 'retailer')
    exclude=('retailer',)
    list_filter= ('product', )
    search_fields= ('id', 'product')
    
    def save_model(self, request, obj, form, change):
        if not obj.retailer:
            obj.retailer = request.user
        super().save_model(request, obj, form, change)

    
        
admin.site.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display= ('id', 'cart', 'product', 'quantity', 'retailer')
    exclude=('retailer',)
    list_filter= ('product', 'quantity')
    search_fields= ('id', 'product', 'quantity','cart')
    
    def save_model(self, request, obj, form, change):
        
        if not obj.retailer:
            obj.retailer = request.user
        super().save_model(request, obj, form, change)

   
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
    

from .models import LoyaltyPoints
@admin.register(LoyaltyPoints)
class LoyaltyPointsAdmin(admin.ModelAdmin):
    list_display = ('order', 'retailer', 'points_gained')
    list_filter = ('retailer',)
    search_fields = ('order__product__name', 'retailer__username')

    def save_model(self, request, obj, form, change):
        # Calculate and set the loyalty points before saving the model
        obj.points_gained = obj.collect_points()
        super().save_model(request, obj, form, change)





    
    
# from django.contrib import admin
# from .models import   Product, Orders, OrderItem
# # Register your models here.


# from fsapp.models import FieldStaff
# from dapp.models import Dealer
# from capp.models import Company
# from rapp.models import Retailer
# from .models import User
# from django.contrib.auth.admin import UserAdmin
# from django.contrib import admin
# from django.db.models import Q
# from itertools import chain
# class CustomUserAdmin(UserAdmin):
#     def get_queryset(self, request):
        
#         # Retrieve the default queryset
#         queryset = super().get_queryset(request)
        
#         # Apply your custom query here
#         # For example, filter users with a specific condition
#         ids = [request.user.id,]
#         if request.user.groups.filter(name='Group_Dealer').exists():
#             queryset1 = FieldStaff.objects.filter(dealer = Dealer.objects.get(dealer=request.user))
#             for i in queryset1:
#                 ids.append(i.fieldstaff.id)
#             queryset2 = Retailer.objects.filter(dealer = Dealer.objects.get(dealer=request.user))
#             for i in queryset2:
#                 ids.append(i.retailer.id)
#             print(ids)
#             queryset = queryset.filter(Q(pk__in=ids))
            
#         elif request.user.groups.filter(name='Group_company').exists():
#             queryset3 = Dealer.objects.filter(company=request.user)
#             for i in queryset3:
#                 ids.append(i.dealer.id)
#             queryset1 = FieldStaff.objects.filter(company=request.user)
#             for i in queryset1:
#                 ids.append(i.fieldstaff.id)
#             queryset2 = Retailer.objects.filter(company=request.user)
#             for i in queryset2:
#                 ids.append(i.retailer.id)
#             queryset = queryset.filter(Q(pk__in=ids))
            
#         elif request.user.groups.filter(name='Group_FieldStaff').exists():
#             queryset2 = Retailer.objects.filter(fieldstaff=FieldStaff.objects.get(fieldstaff=request.user))
#             for i in queryset2:
#                 ids.append(i.retailer.id)
#             queryset = queryset.filter(Q(pk__in=ids))
#         else:
#             pass
        
#         print(queryset)
        
#         return queryset


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# @admin.register(Product)
# class DealerAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if request.user.groups.filter(name='Group_FieldStaff').exists():
#             company = FieldStaff.objects.get(fieldstaff=request.user).company
#             queryset = queryset.filter(company=company)
            
#         if request.user.groups.filter(name='Group_Dealer').exists():
#             company = Dealer.objects.get(dealer=request.user).company
#             queryset = queryset.filter(company=company)

#         if request.user.groups.filter(name='Group_company').exists():
#             company = Company.objects.get(company=request.user).company
#             queryset = queryset.filter(company=company)
                
            
#         return queryset
#     list_display = ('id', 'name', 'category', 'sub_category', 'description', 'price', 'image', 'company' )
   





# @admin.register(Orders)
# class OrderAdmin(admin.ModelAdmin):
    
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
        
#         user = request.user
        
        
#         if user.groups.filter(name='Group_Retailer').exists():
#             retails = Retailer.objects.get(retailer=user)
#             queryset = queryset.filter(retailer__company=retails.company)
     

#         if user.groups.filter(name='Group_FieldStaff').exists():
#             field_staff = FieldStaff.objects.get(fieldstaff=user)
#             queryset = queryset.filter(retailer__company=field_staff.company)
     
        
        
#         if user.groups.filter(name='Group_Dealer').exists():
#             dealer = Dealer.objects.get(dealer=user)
#             queryset = queryset.filter(dealer__company=dealer.company)    
        
#         if request.user.groups.filter(name='Group_company').exists():
#             company = Company.objects.get(company=request.user).company
#             # Filter the queryset to include orders related to the company
#             queryset = queryset.filter(dealer__company=company)

#         return queryset
  
#     list_display = ('id', 'name', 'retailer', 'fieldstaff', 'dealer', 'order_date', 'total_amount')

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
    
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
        
#         if request.user.groups.filter(name='Group_Retailer').exists():
#             retailer = Retailer.objects.get(retailer=request.user)
#             queryset = queryset.filter(order__retailer=retailer)
        
#         if request.user.groups.filter(name='Group_FieldStaff').exists():
#             fieldstaff = FieldStaff.objects.get(fieldstaff=request.user)
#             queryset = queryset.filter(order__fieldstaff=fieldstaff)

#         if request.user.groups.filter(name='Group_Dealer').exists():
#             dealer = Dealer.objects.get(dealer=request.user)
#             queryset = queryset.filter(order__dealer=dealer)

#         if request.user.groups.filter(name='Group_company').exists():
#             company = Company.objects.get(company=request.user).company
#             queryset = queryset.filter(order__dealer__company=company)

#         return queryset


#     list_display = ('order', 'quantity', 'price')