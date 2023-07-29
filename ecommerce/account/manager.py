# # from django.contrib.auth.base_user import BaseUserManager



# # class CustomUserManager(BaseUserManager):
# #     def create_user(self, email_id, Phone_number, password= None, **extra_fields):
# #         if not email_id or Phone_number:
# #             raise ValueError("phone number or email is required")
        
# #         user=self.model(Phone_number=Phone_number, email_id= email_id(self.normalize_email), **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self.db)
        
# #         return user
    
    
# #     def create_superuser(self, email_id, Phone_number, password= None, **extra_fields):
# #         extra_fields.setdefault('is_staff', True)
# #         extra_fields.setdefault('is_superuser', True)
# #         extra_fields.setdefault('is_active', True)
        
# #         return self.create.user(Phone_number/email_id, password, **extra_fields)



from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        username = self.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
    
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(unique=True, max_length=150)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     added_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def _str_(self):
#         return self.username