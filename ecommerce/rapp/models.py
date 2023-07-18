from django.db import models
from dapp.models import Dealer
from capp.models import Company
from fsapp.models import FieldStaff
from django.contrib.auth.models import User
# Create your models here.
class Retailer(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='retailer_profile', blank=True, null=True)
    email_id = models.EmailField(max_length=254,blank=True, null=True)
    ph_no = models.CharField(max_length=20,blank=True, null=True)
    state = models.CharField(max_length=254,blank=True, null=True)
    city = models.CharField(max_length=254,blank=True, null=True)
    zipcode = models.CharField(max_length=10,blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,blank=True, null=True)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE,blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

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