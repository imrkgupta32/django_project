

from django.db import models
from django.contrib.auth.models import User
from capp.models import Company
# class Dealer(models.Model):
    
#     dealer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  


# from django.db import models
# from django.contrib.auth.models import User
# from capp.models import Company

# class Dealer(models.Model):
#     dealer = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

#     def save(self, *args, **kwargs):
#         if self.company_id is not None and not Company.objects.filter(pk=self.company_id).exists():
#             self.company_id = None
#         super().save(*args, **kwargs)


# from django.db import models
# from django.contrib.auth.models import User
# from capp.models import Company

# class Dealer(models.Model):
#     dealer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='dealer_set', blank=True, null=True)
#     # dealer=models.CharField(max_length=254, blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='company_set')




# from django.db import models
# from capp.models import Company
# from django.contrib.auth.models import User
# # Create your models here.
# class Dealer(models.Model):
#     dealer = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company= models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to Company model

    # def __str__(self):
    #     return self.name



# from django.db import models
# from capp.models import Company
# from django.contrib.auth.models import User
# # Create your models here.
# class Dealer(models.Model):
#     dealer = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company= models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to Company model

#     def __str__(self):
#         return self.name


# from django.db import models
# # from capp.models import Company
# from django.contrib.auth.models import User

# # Create your models here.
class Dealer(models.Model):
    # dealer = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    # dealer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dealer_profile', blank=True, null=True)
    email_id = models.EmailField(max_length=254)
    ph_no = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    experience_years = models.IntegerField()
    # company= models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to Company model
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_profile', blank=True, null=True)

    # def __str__(self):
    #     return self.     



#     def assign_fieldstaff(self, username, password):
#         from fsapp.models import FieldStaff  # Imported FieldStaff here to avoid circular import
#         fieldstaff_user = User.objects.create_user(username=username, password=password)
#         fieldstaff = FieldStaff.objects.create(fieldstaff=fieldstaff_user, dealer=self)
#         return fieldstaff

#     def assign_retailer(self, username, password):
#         from rapp.models import Retailer  # Imported Retailer here to avoid circular import
#         retailer_user = User.objects.create_user(username=username, password=password)
#         retailer = Retailer.objects.create(retailer=retailer_user, dealer=self)
#         return retailer


# from django.db import models
# from django.contrib.auth.models import User
# from capp.models import Company

# class Dealer(models.Model):
#     dealer = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company = models.ForeignKey(User, on_delete=models.CASCADE)  

#     def assign_fieldstaff(self, username, password):
#         from fsapp.models import FieldStaff  # Imported FieldStaff here to avoid circular import
#         fieldstaff_user = User.objects.create_user(username=username, password=password)
#         fieldstaff = FieldStaff.objects.create(user=fieldstaff_user, dealer=self)
#         return fieldstaff

#     def assign_retailer(self, username, password):
#         from rapp.models import Retailer  # Imported Retailer here to avoid circular import
#         retailer_user = User.objects.create_user(username=username, password=password)
#         retailer = Retailer.objects.create(user=retailer_user, dealer=self)
#         return retailer
