from django import forms
from .models import Product, Orders, OrderItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'price', 'description', 'sub_category', 'company']


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'retailer', 'fieldstaff', 'dealer', 'order_date', 'total_amount']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']


