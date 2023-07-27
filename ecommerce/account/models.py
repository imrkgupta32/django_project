
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser, Group, Permission,  PermissionsMixin
from .manager import CustomUserManager
from django.utils import timezone
class CustomUser(AbstractUser, PermissionsMixin):
    # email_id = models.EmailField(max_length=100, unique=True)
    # phone_no = PhoneField(blank=True, help_text='Contact phone number', unique=True)
# 
    # USERNAME_FIELD = 'email_id/phone_no' # Use only one field for authentication
    # REQUIRED_FIELDS = []
    objects = CustomUserManager()

    is_Company = models.BooleanField('Is Company', default=False)
    is_Dealer = models.BooleanField('Is Dealer', default=False)
    is_FieldStaff = models.BooleanField('Is FieldStaff', default=False)
    is_Retailer = models.BooleanField('Is Retailer', default=False)

    groups = models.ManyToManyField(Group, related_name='user_custom', related_query_name='custom_user', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_custom', related_query_name='custom_user', blank=True)

    class Meta:
        default_related_name = 'custom_users'



    username = models.CharField(unique=True, max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def _str_(self):
        return self.username
