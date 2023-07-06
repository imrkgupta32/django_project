# from django.contrib.auth.models import Permission
# from django.contrib.auth.models import User



# def create_permissions():
    
#     fieldstaff_permissions = [
#         Permission.objects.get_or_create(
#             codename='assign_retailer',
#             name='Can assign Retailer',
#             content_type=None,  # Replace with the actual content type if needed
#         )[0],
#     ]
#     # Assign permissions to the FieldStaff role
#     FieldStaff = User.objects.get(username='fieldstaff')  
#     FieldStaff.user_permissions.set(fieldstaff_permissions)
    
# create_permissions()




    
#     # Get content type for the User model
#     user_content_type = ContentType.objects.get(app_label='auth', model='user')
#     fieldstaff_permissions = [
#         Permission.objects.get_or_create(
#             codename='assign_retailer',
#             name='Can assign Retailer',
#             content_type=user_content_type,
#         )[0],
#     ]
#     # Add permissions to the Fieldstaff group
#     fieldstaff_group = Group.objects.get(name='Fieldstaff')
#     fieldstaff_group.permissions.set(fieldstaff_permissions)


# create_permissions()