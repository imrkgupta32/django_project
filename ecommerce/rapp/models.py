from django.db import models
from dapp.models import Dealer
from capp.models import Company
from phonenumber_field.modelfields import PhoneNumberField
from fsapp.models import FieldStaff
from django.contrib.auth.models import User
# Create your models here.
class Retailer(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='retailer_profile', blank=True, null=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    email_id = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    phone_number = PhoneNumberField( blank=True, null=True, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.PROTECT, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.PROTECT, related_name='dealer_retailer', blank=True, null=True, default=None)
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_retailer',blank=True, null=True, default=None)
    loyalty_points = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.retailer.username
    
    
    def get_aggregated_orders(self):
        from django.db.models import Sum, F

        aggregated_orders = self.order_items.values('order__id', 'order__order_date').annotate(
            total_amount=Sum(F('product__price') * F('quantity')),
            total_quantity=Sum('quantity')
        ).order_by('order__order_date')
        
        return aggregated_orders
    




# from django.db import models
# from dapp.models import Dealer
# from capp.models import Company
# from fsapp.models import FieldStaff
# from django.contrib.auth.models import User
# # Create your models here.
# class Retailer(models.Model):
#     retailer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='retailer_profile', blank=True, null=True)
#     email_id = models.EmailField(max_length=254,blank=True, null=True)
#     ph_no = models.CharField(max_length=20,blank=True, null=True)
#     state = models.CharField(max_length=254,blank=True, null=True)
#     city = models.CharField(max_length=254,blank=True, null=True)
#     zipcode = models.CharField(max_length=10,blank=True, null=True)
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,blank=True, null=True)
#     fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE,blank=True, null=True)
#     company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return self.retailer.username