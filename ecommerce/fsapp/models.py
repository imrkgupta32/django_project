from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from dapp.models import Dealer
from capp.models import Company
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class FieldStaff(models.Model):
    fieldstaff = models.ForeignKey(User, on_delete=models.PROTECT, related_name='fieldstaff_profile', blank=True, null=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    email_id = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    phone_number = PhoneNumberField( blank=True, null=True, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.PROTECT, related_name='dealer_fieldstaff', blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_fieldstaf', blank=True, null=True)
    
    
    
    def __str__(self):
        return str(self.fieldstaff.username)



















