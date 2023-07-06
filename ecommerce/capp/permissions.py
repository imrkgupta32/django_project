# # from django.contrib.auth.models import Permission
# # from django.contrib.contenttypes.models import ContentType
# # from django.contrib.auth.models import Group
# # from django.contrib.auth.models import User


# # def create_permissions():
# #     # Get content type for the User model
# #     user_content_type = ContentType.objects.get(app_label='auth', model='user')

# #     # Define permissions for Company group
# #     company_permissions = [
# #         Permission.objects.get_or_create(
# #             codename='assign_dealer',
# #             name='Can assign Dealer',
# #             content_type=user_content_type,
# #         )[0],
# #         Permission.objects.get_or_create(
# #             codename='assign_fieldstaff',
# #             name='Can assign Fieldstaff',
# #             content_type=user_content_type,
# #         )[0],
# #         Permission.objects.get_or_create(
# #             codename='assign_retailer',
# #             name='Can assign Retailer',
# #             content_type=user_content_type,
# #         )[0],
# #     ]
# #     # Add permissions to the Company group
# #     company_group = Group.objects.get(name='Company')
# #     company_group.permissions.set(company_permissions)
    
    
# # def create_permissions():
# #     # Define permissions for the Company role
# #     company_permissions = [
# #         Permission.objects.get_or_create(
# #             codename='assign_dealer',
# #             name='Can assign Dealer',
# #             content_type=None,  # Replace with the actual content type if needed
# #         )[0],
# #         Permission.objects.get_or_create(
# #             codename='assign_fieldstaff',
# #             name='Can assign Fieldstaff',
# #             content_type=None,  
# #         )[0],
# #         Permission.objects.get_or_create(
# #             codename='assign_retailer',
# #             name='Can assign Retailer',
# #             content_type=None,  
# #         )[0],
# #     ]
# #     # Assign permissions to the Company role
#     # Company = User.objects.get(username='company')  
#     # Company.user_permissions.set(company_permissions)  
    
    
    

    
# # Call the create_permissions() function to create the permissions
# # create_permissions()

# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType

# def create_permissions():
#     # Get the content type for the User model
#     content_type = ContentType.objects.get(app_label='auth', model='user')
#     # company_group, _ = Group.objects.get_or_create(name='Company')
    
#     # Define and create the permissions for the Company group
#     company_permissions = [
        
#         Permission.objects.get_or_create(
#             codename='assign_dealer',
#             name='Can assign Dealer',
#             content_type=content_type,
#         )[0],
#         Permission.objects.get_or_create(
#             codename='assign_fieldstaff',
#             name='Can assign Fieldstaff',
#             content_type=content_type,
#         )[0],
#         Permission.objects.get_or_create(
#             codename='assign_retailer',
#             name='Can assign Retailer',
#             content_type=content_type,
#         )[0],
#     ]

#     # Assign the permissions to the Company group
#     company_group = Group.objects.get(name='Company')
#     company_group.permissions.set(company_permissions)
    
# create_permissions()
 
#     # Company = User.objects.get(username='company')  
#     # Company.user_permissions.set(company_permissions)  
    
#     # Creating user accounts for the dealer, field staff, and retailer
#     # dealer = User.objects.create_user(username='dealer', password='dealer_password')
#     # fieldstaff = User.objects.create_user(username='fieldstaff', password='fieldstaff_password')
#     # retailer = User.objects.create_user(username='retailer', password='retailer_password')
    
    

# # Calling the create_permissions() function to create and assign the permissions
# # create_permissions()

