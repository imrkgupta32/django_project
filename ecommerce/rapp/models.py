from django.db import models
from dapp.models import Dealer
from capp.models import Company
from fsapp.models import FieldStaff
from django.contrib.auth.models import User
# Create your models here.
class Retailer(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='retailer_profile', blank=True, null=True)
    email_id = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    DEFAULT_COUNTRY_CODE = '+977-' 
    phone_no = models.CharField(max_length=15,default=DEFAULT_COUNTRY_CODE, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.PROTECT, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.PROTECT, related_name='retailers', blank=True, null=True, default=None)
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='retailers',blank=True, null=True, default=None)
    
    
    
    def __str__(self):
        return self.retailer.username
    
    




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