
from django.db import models
from dapp.models import Dealer
from capp.models import Company
from django.contrib.auth.models import User
class FieldStaff(models.Model):
    fieldstaff = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='fieldstaffs',blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fieldstaffs',blank=True, null=True)
    email_id = models.EmailField(max_length=255,blank=True, null=True)
    ph_no = models.CharField(max_length=20,blank=True, null=True)
    state = models.CharField(max_length=254,blank=True, null=True)
    city = models.CharField(max_length=254,blank=True, null=True)
    zipcode = models.CharField(max_length=10,blank=True, null=True)
    experience_years = models.IntegerField()

    
    def __str__(self):
        return str(self.fieldstaff.username)












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









