
from django.db import models
from django.contrib.auth.models import User
from capp.models import Company


# # Create your models here.
class Dealer(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='dealer_profile', blank=True, null=True)
    email_id = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    DEFAULT_COUNTRY_CODE = '+977-' 
    phone_no = models.CharField(max_length=15,default=DEFAULT_COUNTRY_CODE, blank=True, null=True)
    experience_years = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_profile', blank=True, null=True, default=None)
    
    

    def __str__(self):
        return self.dealer.username










# from django.db import models
# from django.contrib.auth.models import User
# from capp.models import Company


# # # Create your models here.
# class Dealer(models.Model):
#     dealer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='dealer_profile', blank=True, null=True)
#     email_id = models.EmailField(max_length=254,blank=True, null=True)
#     ph_no = models.CharField(max_length=15,blank=True, null=True)
#     state = models.CharField(max_length=50,blank=True, null=True)
#     city = models.CharField(max_length=50,blank=True, null=True)
#     zipcode = models.CharField(max_length=10,blank=True, null=True)
#     experience_years = models.IntegerField()
#     company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_profile', blank=True, null=True)

#     def __str__(self):
#         return self.dealer.username

