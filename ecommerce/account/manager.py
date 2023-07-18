# from django.contrib.auth.base_user import BaseUserManager



# class UserManager(BaseUserManager):
#     def create_user(self, email_id, Phone_number, password= None, **extra_fields):
#         if not email_id or Phone_number:
#             raise ValueError("phone number or email is required")
        
#         user=self.model(Phone_number=Phone_number, email_id= email_id(self.normalize_email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
        
#         return user
    
    
#     def create_superuser(self, email_id, Phone_number, password= None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
        
#         return self.create.user(Phone_number/email_id, password, **extra_fields)