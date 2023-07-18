from django import forms
from .models import Dealer

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['dealer', 'email_id', 'ph_no', 'state', 'city', 'zipcode', 'experience_years', 'company']
