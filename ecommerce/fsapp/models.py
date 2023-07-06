from django.db import models
from dapp.models import Dealer
from capp.models import Company
from django.contrib.auth.models import User
# Create your models here.
# class FieldStaff(models.Model):
#     # fieldstaff = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#     fieldstaff = models.CharField(max_length=254, blank=True, null=True)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=254)
#     city = models.CharField(max_length=254)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     company = models.ForeignKey(User, on_delete=models.CASCADE)  # Add ForeignKey to Company model

    # def __str__(self):
    #     print(f"Name: {self.name}")
    #     return str(self.name) if self.name else 'Unnamed FieldStaff'


# from django.db import models
# from dapp.models import Dealer
# from capp.models import Company
# from django.contrib.auth.models import User
# # Create your models here.
# class FieldStaff(models.Model):
#     name = models.CharField(max_length=254, blank=True, null=True)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=254)
#     city = models.CharField(max_length=254)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     company = models.ForeignKey(User, on_delete=models.CASCADE)  # Add ForeignKey to Company model


# from django.db import models
# from dapp.models import Dealer
# from capp.models import Company
# from django.contrib.auth.models import User
# # Create your models here.
# class FieldStaff(models.Model):
#     name = models.CharField(max_length=254, blank=True, null=True)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=254)
#     city = models.CharField(max_length=254)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     company = models.ForeignKey(User, on_delete=models.CASCADE)  # Add ForeignKey to Company model

#     def __str__(self):
#         return str(self.name) if self.name else 'Unnamed FieldStaff'

# from django.db import models
# from django.contrib.auth.models import User
# from dapp.models import Dealer
# from capp.models import Company


class FieldStaff(models.Model):
    # fieldstaff = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, blank=True, null=True)
    email_id = models.EmailField(max_length=255)
    ph_no = models.CharField(max_length=20)
    state = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    zipcode = models.CharField(max_length=10)
    experience_years = models.IntegerField()

#     def assign_retailer(self, username, password):
#         from rapp.models import Retailer  # Imported Retailer here to avoid circular import
#         retailer_user = User.objects.create_user(username=username, password=password)
#         retailer = Retailer.objects.create(user=retailer_user, dealer=self.dealer, fieldstaff=self)
#         return retailer
