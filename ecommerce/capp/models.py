from django.db import models
from django.contrib.auth.models import User

# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
    

#     def __str__(self):
#         return self.name






class Company(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    email_id = models.EmailField(max_length=255)
    ph_no = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    

    def __str__(self):
        return self.company.username



# class Company(models.Model):
#     # compnay= models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
#     compnay= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)

#     def assign_dealer(self, username, password):
#         dealer_user = User.objects.create_user(username=username, password=password)
#         dealer = Dealer.objects.create(user=dealer_user)
#         return dealer

#     def assign_fieldstaff(self, username, password):
#         fieldstaff_user = User.objects.create_user(username=username, password=password)
#         fieldstaff = FieldStaff.objects.create(user=fieldstaff_user, dealer=self.dealer)
#         return fieldstaff

#     def assign_retailer(self, username, password):
#         retailer_user = User.objects.create_user(username=username, password=password)
#         retailer = Retailer.objects.create(user=retailer_user, fieldstaff=self.fieldstaff)
#         return retailer




# from django.db import models
# from django.contrib.auth.models import User
# from dapp.models import Dealer
# from fsapp.models import FieldStaff
# from rapp.models import Retailer

# class Company(models.Model):
#     company = models.ForeignKey(User, on_delete=models.CASCADE) #related_name='company_profile')
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)

#     def assign_dealer(self, username, password):
#         dealer_user = User.objects.create_user(username=username, password=password)
#         dealer = Dealer.objects.create(user=dealer_user, company=self)
#         return dealer

#     def assign_fieldstaff(self, username, password):
#         fieldstaff_user = User.objects.create_user(username=username, password=password)
#         fieldstaff = FieldStaff.objects.create(user=fieldstaff_user, company=self)
#         return fieldstaff

#     def assign_retailer(self, username, password):
#         retailer_user = User.objects.create_user(username=username, password=password)
#         retailer = Retailer.objects.create(user=retailer_user, company=self)
#         return retailer


# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email_id, password, **extra_fields):
#         if not email_id:
#             raise ValueError('The Email field must be set')
#         email_id = self.normalize_email(email_id)
#         user = self.model(email=email_id, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email_id, password='default', **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email_id, password, **extra_fields)

#     def create_superuser(self, email_id, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email_id, password, **extra_fields)

# class Company(AbstractUser):
#     name = models.CharField(max_length=255)
#     email_id = models.EmailField(max_length=255, unique=True)
#     ph_no = models.CharField(max_length=20)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
    
#     USERNAME_FIELD = 'email_id'
#     REQUIRED_FIELDS = ['name']
    
#     objects = CustomUserManager()
    
#     def __str__(self):
#         return self.name



# from django.db import models
# from django.contrib.auth.models import User

# class Company(models.Model):
#     company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_profile', blank=True, null=True)
#     email_id = models.EmailField(max_length=255)
#     ph_no = models.CharField(max_length=10)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
    
    
    
    # def assign_dealer(id, username, password):
    #     from dapp.models import Dealer  # Import Dealer here to avoid circular import
    #     dealer_user = User.objects.create_user(username=username, password=password)
    #     dealer = Dealer.objects.create(user=dealer_user, company=id)
    #     return dealer

    # def assign_fieldstaff(id, username, password):
    #     from fsapp.models import FieldStaff  # Import FieldStaff here to avoid circular import
    #     fieldstaff_user = User.objects.create_user(username=username, password=password)
    #     fieldstaff = FieldStaff.objects.create(user=fieldstaff_user, company=id)
    #     return fieldstaff

    # def assign_retailer(id, username, password):
    #     from rapp.models import Retailer  # Import Retailer here to avoid circular import
    #     retailer_user = User.objects.create_user(username=username, password=password)
    #     retailer = Retailer.objects.create(user=retailer_user, company=id)
    #     return retailer


    
    

    # def assign_dealer(self, username, password):
    #     from dapp.models import Dealer  # Import Dealer here to avoid circular import
    #     dealer_user = User.objects.create_user(username=username, password=password)
    #     dealer = Dealer.objects.create(user=dealer_user, company=self)
    #     return dealer

    # def assign_fieldstaff(self, username, password):
    #     from fsapp.models import FieldStaff  # Import FieldStaff here to avoid circular import
    #     fieldstaff_user = User.objects.create_user(username=username, password=password)
    #     fieldstaff = FieldStaff.objects.create(user=fieldstaff_user, company=self)
    #     return fieldstaff

    # def assign_retailer(self, username, password):
    #     from rapp.models import Retailer  # Import Retailer here to avoid circular import
    #     retailer_user = User.objects.create_user(username=username, password=password)
    #     retailer = Retailer.objects.create(user=retailer_user, company=self)
    #     return retailer

