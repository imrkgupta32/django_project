# from django.contrib.auth.models import Permission
# from django.contrib.auth.models import User


# def create_permissions():
    
#     dealer_permissions = [
#         Permission.objects.get_or_create(
#             codename='assign_fieldstaff',
#             name='Can assign Fieldstaff',
#             content_type=None,  # Replace with the actual content type if needed
#         )[0],
#         Permission.objects.get_or_create(
#             codename='assign_retailer',
#             name='Can assign Retailer',
#             content_type=None,  
#         )[0],
#     ]
#     # Assigning permissions to the Dealer role
#     Dealer = User.objects.get(username='dealer')  
#     Dealer.user_permissions.set(dealer_permissions)
    
# create_permissions()



# # Get content type for the User model
#     # user_content_type = ContentType.objects.get(app_label='auth', model='user')
#     # dealer_permissions = [
#     #     Permission.objects.get_or_create(
#     #         codename='assign_fieldstaff',
#     #         name='Can assign Fieldstaff',
#     #         content_type=user_content_type,
#     #     )[0],
#     #     Permission.objects.get_or_create(
#     #         codename='assign_retailer',
#     #         name='Can assign Retailer',
#     #         content_type=user_content_type,
#     #     )[0],
#     # ]
#     # # Add permissions to the Dealer group
#     # dealer_group = Group.objects.get(name='Dealer')
#     # dealer_group.permissions.set(dealer_permissions)
    