
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser, Group, Permission
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    email_id = models.EmailField(max_length=100, unique=True)
    phone_no = PhoneField(blank=True, help_text='Contact phone number', unique=True)

    USERNAME_FIELD = 'email_id/phone_no' # Use only one field for authentication
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    is_Company = models.BooleanField('Is Company', default=False)
    is_Dealer = models.BooleanField('Is Dealer', default=False)
    is_FieldStaff = models.BooleanField('Is FieldStaff', default=False)
    is_Retailer = models.BooleanField('Is Retailer', default=False)

    groups = models.ManyToManyField(Group, related_name='user_custom', related_query_name='custom_user', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_custom', related_query_name='custom_user', blank=True)

    class Meta:
        default_related_name = 'custom_users'


