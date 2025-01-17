from django import forms
from .models import Customer, Product, Purchase

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer', 'product', 'quantity']