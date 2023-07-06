# from django.contrib import admin
# from .models import  FieldStaff
# # Register your models here.
# @admin.register(FieldStaff)
# class FieldStaffAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'ph_no', 'email_id', 'state', 'city', 'zipcode', 'experience_years', 'dealer', 'company')


# from django.contrib import admin
# from .models import FieldStaff

# @admin.register(FieldStaff)
# class FieldStaffAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:
#             queryset = queryset.filter(company=request.user)
#         return queryset
#     list_display = ('id', 'name', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'dealer', 'company' )


from django.contrib import admin
from .models import FieldStaff

@admin.register(FieldStaff)
class FieldStaffAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(company=request.user)
        return queryset
    list_display = ('id', 'email_id', 'ph_no','state', 'city', 'zipcode','experience_years', 'dealer', 'company' )

