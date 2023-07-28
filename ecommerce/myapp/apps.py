from django.apps import AppConfig
from django.dispatch import receiver
# from myapp.signals import order_placed
# from myapp.models import Orders
# from myapp.models import Notification

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'


    
    def ready(self):
        # Import the signal and signal handler
        from .signals import order_placed
        from .models import Notification
        from myapp.models import Orders
        # import myapp.signals 
        from myapp.models import send_merchant_notification
        order_placed.connect(send_merchant_notification, sender=Orders)
        # Connect the signal handler to the signal
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


    
       
       
        