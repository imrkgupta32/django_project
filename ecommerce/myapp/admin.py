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
class DealerAdmin(admin.ModelAdmin):
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
    list_display = ('id', 'name', 'category', 'sub_category', 'description', 'price', 'image', 'company' )
    list_filter = ('category', 'sub_category', )
    search_fields = ('id', 'name', 'category', 'sub_category', 'description', 'price', 'company' )
   
   
   
   

from myapp.models import Category
from myapp.models import Review
from myapp.models import Rating

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if request.user.groups.filter(name='Group_company').exists():
    #         company = Company.objects.get(company=request.user).company
    #         queryset = queryset.filter(company=company)
            
    #     return queryset    
    list_display = ('id', 'name')
    search_fields = ('name',)
    
    

# Register the Review model in the admin site
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'retailer', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('retailer__username', 'product__name')


# Register the Rating model in the admin site
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'product', 'rating')
    list_filter = ('rating',)
    search_fields = ('retailer__username', 'product__name')







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
  
    list_display = ('id', 'name', 'retailer', 'fieldstaff', 'dealer', 'order_date', 'total_amount')
    list_filter = ('order_date',)
    search_fields = ('id', 'name', 'retailer', 'fieldstaff', 'dealer', 'order_date')

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


    list_display = ('order', 'quantity', 'price')
    list_filter = ( 'quantity', )
    search_fields = ('order', 'quantity', 'price')
    
    
    
    
    
    
    
    
    
    
    
    
    
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