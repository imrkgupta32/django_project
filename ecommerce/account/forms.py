# from django import forms
# from django .contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class LoginForm(forms.form):
#     username =forms.CharField(
#         wedget= forms.TextInput(
#             attrs={
#                 "class": "form.control"
#             }
#         )
#     )

#     password =forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form.control"
#             }
#         )
#     )


# class SignUPForm(UserCreationForm):
#     username =forms.CharField(
#         wedget= forms.TextInput(
#             attrs={
#                 "class": "form.control"
#             }
#         )
#     )

#     password1 =forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form.control"
#             }
#         )
#     )
    
    
#     password2 =forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form.control"
#             }
#         )
#     )
    
    
#     email =forms.CharField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form.control"
#             }
#         )
#     )
    
    
    
#     class Meta:
#         Models =CustomUser
#         fields= ('username', 'email', 'password1', 'password2', 'is_company', 'is_dealer', 'is_fieldstaff', 'is_retailer')