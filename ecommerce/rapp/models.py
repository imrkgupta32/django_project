from django.db import models
from dapp.models import Dealer
from capp.models import Company
from fsapp.models import FieldStaff
from django.contrib.auth.models import User
# Create your models here.
class Retailer(models.Model):
    # retailer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    email_id = models.EmailField(max_length=254)
    ph_no = models.CharField(max_length=20)
    state = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    zipcode = models.CharField(max_length=10)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Add ForeignKey to Company model

    # def __str__(self):
    #     return self.name
    
    
# class Retailer(models.Model):
#     # retailer = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#     retailer = models.CharField(max_length=254, blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=254)
#     city = models.CharField(max_length=254)
#     zipcode = models.CharField(max_length=10)
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE)
#     company = models.ForeignKey(User, on_delete=models.CASCADE)  # Add ForeignKey to Company model
