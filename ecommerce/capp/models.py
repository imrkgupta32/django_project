from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Company(models.Model):
    company = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    email_id = models.EmailField(max_length=200, blank=True, null=True, unique=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True, default='')
    city = models.CharField(max_length=50, blank=True, null=True, default='')
    zipcode = models.CharField(max_length=10, blank=True, null=True, default='')
   
    


    def __str__(self):
        return self.company.username





# from django.db import models
# from django.contrib.auth.models import User


# class Company(models.Model):
#     company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     email_id = models.EmailField(max_length=255,blank=True, null=True)
#     ph_no = models.CharField(max_length=20,blank=True, null=True)
#     state = models.CharField(max_length=50,blank=True, null=True)
#     city = models.CharField(max_length=50,blank=True, null=True)
#     zipcode = models.CharField(max_length=10,blank=True, null=True)
    

#     def __str__(self):
#         return self.company.username




