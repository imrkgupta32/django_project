from django import forms
from .models import FieldStaff

class FieldStaffForm(forms.ModelForm):
    class Meta:
        model = FieldStaff
        fields = ['fieldstaff', 'dealer', 'company', 'email_id', 'ph_no', 'state', 'city', 'zipcode', 'experience_years']
