from django.db import models
from capp.models import Company
from dapp.models import Dealer
from rapp.models import Retailer
from fsapp.models import FieldStaff
from django.contrib.auth.models import User
# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
    

#     def __str__(self):
#         return self.name


# class Dealer(models.Model):
#     name = models.CharField(max_length=254)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     company= models.ForeignKey(Company, on_delete=models.CASCADE)  # Add ForeignKey to Company model

#     def __str__(self):
#         return self.name


# class FieldStaff(models.Model):
#     name = models.CharField(max_length=254)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=254)
#     city = models.CharField(max_length=254)
#     zipcode = models.CharField(max_length=10)
#     experience_years = models.IntegerField()
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Add ForeignKey to Company model

#     def __str__(self):
#         return self.name

# class Retailer(models.Model):
#     name = models.CharField(max_length=254)
#     email_id = models.EmailField(max_length=254)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=254)
#     city = models.CharField(max_length=254)
#     zipcode = models.CharField(max_length=10)
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Add ForeignKey to Company model

#     def __str__(self):
#         return self.name

class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name



class Orders(models.Model):
    name = models.CharField(max_length=254)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order)
