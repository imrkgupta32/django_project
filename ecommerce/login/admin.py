from django.contrib import admin

# Register your models here.
from .models import Profile
from django.db.models import Count
from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "role", "is_active")
    list_filter = ("is_active", "role", "created_at")
    
    
admin.site.register(Profile, ProfileAdmin)
