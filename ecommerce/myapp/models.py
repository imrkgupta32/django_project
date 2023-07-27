from django.db import models
from dapp.models import Dealer
from rapp.models import Retailer
from fsapp.models import FieldStaff
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver



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
    main_category=models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    sub_category = models.CharField(max_length=50,blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    
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
        default='s',
        help_text='Product location status',
    )

    
    def __str__(self):
        return str(self.name)

# @receiver(pre_save, sender=Product)
# def set_default_company(sender, instance, **kwargs):
#     if not instance.company:
#         instance.company = instance.name




class Review(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Rating(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
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
    company = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    order_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=ORDERED_STATUS,
        blank=True,
        default='o',
        help_text='order availability',
    )
    

    def __str__(self):
        return str(self.product)

    
    


     
# from .utils import calculate_loyalty_points
class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE,blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    retailer= models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='order_items', blank=True, null=True)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return str(self.order)
    
    
    
    
    def save(self, *args, **kwargs):
        if not self.total_amount:
            # Retrieve the price of the associated product
            product_price = self.product.price if self.product else Decimal('0.00')
            # Calculate the total amount based on the quantity and product price
            self.total_amount = product_price * self.quantity
               
        super(OrderItem, self).save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.total_amount:
            # Retrieve the price of the associated product
            product_price = self.product.price if self.product else Decimal('0.00')
            # Calculate the total amount based on the quantity and product price
            self.total_amount = product_price * self.quantity

            # Calculate and update the loyalty points earned by the retailer
            loyalty_points_earned = int(self.total_amount)  # 1 point for every Rs 1 spent
            self.retailer.loyalty_points += loyalty_points_earned
            self.retailer.save()

        super(OrderItem, self).save(*args, **kwargs)
    
    
    
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=OrderItem)
def update_total_amount(sender, instance, **kwargs):
    instance.total_amount = instance.product.price * instance.quantity
    
    
from decimal import Decimal      


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    retailer= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.product)

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    retailer= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.cart)

    def save(self, *args, **kwargs):
        if not self.price:
            # Retrieve the price of the associated product
            product_price = self.product.price if self.product else Decimal('0.00')
            # Calculate the total price based on the quantity and product price
            total_price = product_price * self.quantity
            # Set the calculated price in the price field
            self.price = total_price

        super(CartItem, self).save(*args, **kwargs)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)



from django.dispatch import receiver
from myapp.signals import order_placed
from myapp.models import Notification

@receiver(order_placed)
def send_merchant_notification(sender, order, user, **kwargs):
    # Create notification for field staff
    Notification.objects.create(user=user, message='A new order has been placed by a retailer.')

    # Create notification for dealer
    dealer = order.dealer
    Notification.objects.create(user=dealer, message='A new order has been placed by a retailer.')

    # Create notification for company
    company = user.company  # Assuming the user is associated with a company
    Notification.objects.create(user=company, message='A new order has been placed by a retailer.')






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
    
    
    
    
# class LoyaltyPoints(models.Model):
#     order = models.OneToOneField(Orders,on_delete=models.CASCADE,blank=True,null=True)
#     retailer= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     points_gained = models.IntegerField(default=0)

#     def collect_points(self):
#         # Define loyalty points conversion rates
#         conversion_rates = {
#             (0, 100): Decimal('0.005'),   # 0.5% for orders between $0 and $100
#             (101, 200): Decimal('0.01'),  # 1% for orders between $101 and $200
#             # Add more ranges and conversion rates as needed...
#         }

#         # Calculate loyalty points based on the order amount
#         total_amount = self.order.total_amount  # Assuming total_amount is a DecimalField in the Orders model
#         loyalty_points = 0
#         for amount_range, conversion_rate in conversion_rates.items():
#             if amount_range[0] <= total_amount <= amount_range[1]:
#                 loyalty_points = int(total_amount * conversion_rate)
#                 break

#         # Get the retailer's total number of transactions
#         retailer_transactions = self.retailer.order_set.count()  # Assuming retailer is a ForeignKey in LoyaltyPoints

#         # Define transaction-based bonuses
#         transaction_bonuses = {
#             5: 50,   # Earn 50 extra points for 5 transactions
#             10: 100, # Earn 100 extra points for 10 transactions
#             # Add more transaction milestones and bonuses as needed...
#         }

#         # Calculate transaction-based bonuses
#         for transaction_milestone, bonus_points in transaction_bonuses.items():
#             if retailer_transactions >= transaction_milestone:
#                 loyalty_points += bonus_points

#         # Return the total loyalty points
#         return loyalty_points