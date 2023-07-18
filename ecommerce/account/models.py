# from django.db import models
# from phone_field import PhoneField
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from .manager import UserManager

# class CustomeUser(AbstractUser):
    
#     username =None
#     email_id= models.EmailField(max_length=100,  unique=True)
#     phone_no=PhoneField(blank=True, help_text='Contact phone number', unique=True)
#     # user_profile_image = models.ImageField(upload_to="profile")


#     USERNAME_FIELD= 'email_id/phone_no'
#     REQUIRED_FIELDS=[]
#     objects= UserManager()
    
    
    
    
    
# # class CustomUser(AbstractUser):
# #     is_Company = models.BooleanField('Is Company', default=False)
# #     is_Dealer = models.BooleanField('Is Dealer', default=False)
# #     is_FieldStaff = models.BooleanField('Is FieldStaff', default=False)
# #     is_Retailer = models.BooleanField('Is Retailer', default=False)
# #     groups = models.ManyToManyField(Group, related_name='custom_users', related_query_name='custom_user')
# #     user_permissions = models.ManyToManyField(Permission, related_name='custom_users', related_query_name='custom_user')

# #     class Meta:
# #         # Provide a unique related name for the reverse accessor
# #         default_related_name = 'custom_users'


