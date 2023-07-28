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


ORDER_LOCATION_STATUS = (
    ('w', 'Warehouse'),
    ('s', 'In Store'),
    ('t', 'In Transit'),
    ('d', 'Delivered'),
)


from django.db.models import Sum
class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE,blank=True, null=True)
    fieldstaff = models.ForeignKey(FieldStaff, on_delete=models.CASCADE,blank=True, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    order_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_purchase = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=ORDERED_STATUS,
        blank=True,
        default='o',
        help_text='order availability',
    )
    
    
    
    order_location = models.CharField(
        max_length=1,
        choices=PRODUCT_LOCATION_STATUS,
        blank=True,
        default='s',
        help_text='Product location status',
    )

    def __str__(self):
        return str(self.product)

    
    
    @property
    def total_purchase(self):
        return self.orderitem_set.aggregate(total_purchase=Sum('total_amount'))['total_purchase'] or 0.0
    
    
    @total_purchase.setter
    def total_purchase(self, value):
        self._total_purchase = value
    
    
    
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
               
    # def save(self, *args, **kwargs):   
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
    



@receiver(pre_save, sender=OrderItem)
def update_total_amount(sender, instance, **kwargs):
    instance.total_amount = instance.product.price * instance.quantity
    
 
    
from django.db.models.signals import pre_save
from django.dispatch import receiver    
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






