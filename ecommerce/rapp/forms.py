from django import forms
from .models import Retailer

class RetailerForm(forms.ModelForm):
    class Meta:
        model = Retailer
        fields = ['retailer', 'email_id', 'ph_no', 'state', 'city', 'zipcode', 'dealer', 'fieldstaff', 'company']
