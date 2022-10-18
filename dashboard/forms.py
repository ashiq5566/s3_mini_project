from pyexpat import model
from tkinter.ttk import Widget
from django import forms
from django.forms import HiddenInput
from .models import Customer, PurchaseOrder, Vendor, Item, PurchasedItems,PurchaseOrder,Payment
from django.db.models import Q, Max, F


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_address', 'customer_mobile']
        
        widgets = {
            "customer_name": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Entre name",
                    "label": "Name",
                }
            ),
            "customer_address": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter Address",
                    "label": "Address",
                }
            ),
            "customer_mobile": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter Mobile",
                    "label": "Mobile",
                }
            ),
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_address', 'vendor_mobile']
        
        widgets = {
            "vendor_name": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Entre name",
                    "label": "Name",
                }
            ),
            "vendor_address": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter Address",
                    "label": "Address",
                }
            ),
            "vendor_mobile": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Enter Mobile",
                    "label": "Mobile",
                }
            ),
        }
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'unit_price']
        
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Entre name1",
                    "label": "Name",
                }
            ),
            "unit_price": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Entre price1",
                    "label": "Price",
                }
            ),
        }

class PurchasedItemForm(forms.ModelForm):

    class Meta:
        model = PurchasedItems
        fields = ['item_id', 'quantity','unit_price']
        
        ch = list(Item.objects.all().values('item_id'))
        widgets = {
            "item_id": forms.Select(
                choices=ch,
                attrs={
                    "required": True,
                }
            
            ),
            
        }
# po_n = 101 if PurchaseOrder.objects.count() == 0 else PurchaseOrder.objects.aggregate(max=Max('po_no'))["max"] + 1       
class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['vendor_id']
        
        ch1 = list(Vendor.objects.all().values('vendor_id'))
        widgets = {
           
            "vendor_id": forms.Select(
                choices=ch1,
                attrs={
                    "required": True,
                }
            
            ),
            
        }

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['qty_purchased']
    
# class SelectVendorForm(forms.Form):
#     ch2 = list(Vendor.objects.all().values('vendor_id'))
#     vendor_id = forms.ChoiceField(choices=ch2)
# class SelectVendorForm(forms.ModelForm):
#     class Meta:
#         model = PurchaseOrder
#         fields = ['vendor_id']
        
#         c = list(Vendor.objects.all().values('vendor_id'))
#         widgets = {
           
#             "vendor_id": forms.Select(
#                 choices=c,
#                 attrs={
#                     "required": True,
#                 }
            
#             ),
            
#         }