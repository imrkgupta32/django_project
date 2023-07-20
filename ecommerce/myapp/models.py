from django.db import models
# from capp.models import Company
from dapp.models import Dealer
from rapp.models import Retailer
from fsapp.models import FieldStaff
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name 


class Product(models.Model):
    
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_profile', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    sub_category = models.CharField(max_length=50,blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name



class Review(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])




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
    
    
    
    
