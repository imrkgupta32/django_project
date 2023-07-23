from django.db import models
from django.contrib.auth.models import User
# from .models import Company, Dealer, FieldStaff
# Create your models here.
class Profile(models.Model) :
    Role_choices = (
        (1, 'Company'),
        (2, 'Dealer'),
        (3, 'FieldStaff'),
        (4, 'Retailer'),
    )
    
    
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank= True)
    role= models.PositiveSmallIntegerField(choices=Role_choices, null=True, blank=True)
    is_active= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # user_count= models.IntegerField(null=True, blank=True)
    
    @property
    def email(self):
        return "%s"%(self.user.email)
    
    def __str__(self) :
        return self.user.username
    
    