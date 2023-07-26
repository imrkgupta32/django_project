from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company', 'email_id', 'phone_no', 'address', 'nationality', 'state', 'city', 'zipcode']
