from pyexpat import model
from django import forms
from .models import Customer, Vendor, Item

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'customer_name', 'customer_address', 'customer_mobile']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_id', 'vendor_name', 'vendor_address', 'vendor_mobile']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_id', 'name', 'unit_price']
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['product','order_quantity']