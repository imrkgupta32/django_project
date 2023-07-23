from django.db import models
# from capp.models import Company
from dapp.models import Dealer
from rapp.models import Retailer
from fsapp.models import FieldStaff
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name


PRODUCT_STATUS = (
    ('a', 'Available'),
    ('o', 'Out of stock'),
    ('w', 'Way to deliver'),
    ('d', 'Delivered'),
    ('c', 'Cancelled')
)


PRODUCT_LOCATION_STATUS = (
    ('w', 'Warehouse'),
    ('s', 'In Store'),
    ('t', 'In Transit'),
    ('d', 'Delivered'),
)

class Product(models.Model):
    
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    main_category=models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)   #while adding category with fk django.db.utils.DataError: invalid input syntax for type bigint: "copy"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    sub_category = models.CharField(max_length=50,blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=PRODUCT_STATUS,
        blank=True,
        default='a',
        help_text='Product availability',
    )
    
    
    location_status = models.CharField(
        max_length=1,
        choices=PRODUCT_LOCATION_STATUS,
        blank=True,
        default='w',
        help_text='Product location status',
    )

    
    
    
    def __str__(self):
        return self.name



class Review(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])



ORDERED_STATUS = (
    ('r', 'received'),
    ('c', 'cancelled'),
    ('o', 'ordered'),
    
    
)



class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE,blank=True, null=True)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE,blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,blank=True, null=True)
    order_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=1,
        choices=ORDERED_STATUS,
        blank=True,
        default='o',
        help_text='order availability',
    )
    

    def __str__(self):
        return str(self.product)


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE,blank=True, null=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order)
    
    
 
 
 
from django.db.models import F, Sum
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    price= models.DecimalField( default=0.00, max_digits=100, decimal_places=2)
    
    

class CartItem(models.Model):
    cart=models.ForeignKey('Cart',on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    total_price= models.DecimalField( default=0.00, max_digits=100, decimal_places=2)  
    
    
    @property
    def total_price(self):
        return self.cartitem_set.aggregate(
            total_price=Sum(F('quantity') * F('product__price'))
        )['total_price']  
    
    



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
    
    
    
    
