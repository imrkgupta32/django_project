
from django.dispatch import Signal

order_placed = Signal()





# @receiver(pre_save, sender=OrderItem)
# def calculate_total_amount(sender, instance, **kwargs):
#     if instance.product and instance.product.price is not None:
#         instance.total_amount = instance.quantity * instance.product.price
#     else:
#         instance.total_amount = Decimal('0.00')

# # signals.py
# from django.dispatch import receiver
# # from yourapp.signals import order_placed
# from myapp.models import Notification

# @receiver(order_placed)
# def send_merchant_notification(sender, order, user, **kwargs):
#     # Create notification for field staff
#     Notification.objects.create(user=user, message='A new order has been placed by a retailer.')

#     # Create notification for dealer
#     dealer = order.dealer
#     Notification.objects.create(user=dealer, message='A new order has been placed by a retailer.')

#     # Create notification for company
#     company = user.company  # Assuming the user is associated with a company
#     Notification.objects.create(user=company, message='A new order has been placed by a retailer.')
