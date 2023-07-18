from django.db import models
# from capp.models import Company
from dapp.models import Dealer
from rapp.models import Retailer
from fsapp.models import FieldStaff
from django.contrib.auth.models import User


class Product(models.Model):
    
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    sub_category = models.CharField(max_length=50,blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name



class Orders(models.Model):
    name = models.CharField(max_length=254,blank=True, null=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE,blank=True, null=True)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE,blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,blank=True, null=True)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE,blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order)
    
    
    
    



# from django.db import models
# # from capp.models import Company
# from dapp.models import Dealer
# from rapp.models import Retailer
# from fsapp.models import FieldStaff
# from django.contrib.auth.models import User


# class Product(models.Model):
    
#     name = models.CharField(max_length=254)
#     image = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     category = models.CharField(max_length=50, blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField(blank=True, null=True)
#     sub_category = models.CharField(max_length=50,blank=True, null=True)
#     company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
#     def __str__(self):
#         return self.name



# class Orders(models.Model):
#     name = models.CharField(max_length=254,blank=True, null=True)
#     retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE,blank=True, null=True)
#     fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE,blank=True, null=True)
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,blank=True, null=True)
#     order_date = models.DateField()
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
   

#     def __str__(self):
#         return self.name


# class OrderItem(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE,blank=True, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return str(self.order)
    
    
    
    
