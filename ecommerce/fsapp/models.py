from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from dapp.models import Dealer
from capp.models import Company
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class FieldStaff(models.Model):
    fieldstaff = models.ForeignKey(User, on_delete=models.PROTECT, related_name='fieldstaff_profile', blank=True, null=True)
    email_id = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    phone_number = PhoneNumberField( blank=True, null=True, unique=True)
    experience_years = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.PROTECT, related_name='dealer_fieldstaff', blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_fieldstaf', blank=True, null=True)
    
    
    
    def __str__(self):
        return str(self.fieldstaff.username)


# @receiver(pre_save, sender=FieldStaff)
# # def set_default_dealer(sender, instance, **kwargs):
# #     if not instance.dealer and instance.fieldstaff:
# #         try:
# #             # Find the associated Dealer based on some criteria (e.g., email or phone number)
# #             associated_dealer = Dealer.objects.get(email_id=instance.fieldstaff.email)
# #             instance.dealer = associated_dealer
# #         except Dealer.DoesNotExist:
# #             pass


# def set_default_dealer(sender, instance, **kwargs):
#     if not instance.dealer:
#         instance.dealer = instance.dealer








# from django.db import models
# from dapp.models import Dealer
# from capp.models import Company
# from django.contrib.auth.models import User
# class FieldStaff(models.Model):
#     fieldstaff = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='fieldstaffs',blank=True, null=True)
#     company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fieldstaffs',blank=True, null=True)
#     email_id = models.EmailField(max_length=255,blank=True, null=True)
#     ph_no = models.CharField(max_length=20,blank=True, null=True)
#     state = models.CharField(max_length=254,blank=True, null=True)
#     city = models.CharField(max_length=254,blank=True, null=True)
#     zipcode = models.CharField(max_length=10,blank=True, null=True)
#     experience_years = models.IntegerField()

    
#     def __str__(self):
#         return str(self.fieldstaff.username)









