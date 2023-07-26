from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Customize the User admin as per your requirements
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    # search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

# If you have any other models to register, import them and register them here.

# Example: Registering the Dealer model
# from .models import Dealer

# @admin.register(Dealer)
# class DealerAdmin(admin.ModelAdmin):
#     list_display = ('dealer', 'email_id', 'phone_no', 'experience_years', 'address')
#     search_fields = ('dealer__username', 'dealer__email', 'email_id', 'phone_no')
#     # Customize other fields and admin options as per your requirements

# If you have any other models to register, import them and register them here.

