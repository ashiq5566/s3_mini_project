from email.policy import default
import uuid
from django.db import models
# from dashboard.views import product
from django.contrib.auth.models import User
ID_FIELD_LENGTH = 16
import random, string

# Create your models here.  
class MyUUIDModel(models.Model):
    userid = models.CharField(max_length=36,default = uuid.uuid4)
    regnumber = models.IntegerField(null=True)
    regnumber1 = models.CharField(primary_key=True,max_length=15,null=False)
    username = models.CharField(max_length= 100, null=True)
    def __str__(self):
        return self.username
    
class Item(models.Model):
        item_no = models.IntegerField(null=True)
        item_id = models.CharField(max_length=10,null=True)
        name = models.CharField(max_length=100, null=True, blank=False)
        unit_price = models.PositiveBigIntegerField(null=True,blank=True)
        qty_available = models.PositiveIntegerField(null=True, default=0)
        qty_sold = models.PositiveIntegerField(null=True, default=0)
        status = models.BooleanField(default=False)
        
        def __str__(self):
            return self.item_id
     
    
class Customer(models.Model):
    customer_no = models.IntegerField(null=True)
    customer_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    customer_name = models.CharField(max_length=100,null=True)
    customer_address = models.CharField(max_length=200,null=True)
    customer_mobile = models.CharField(max_length=15,null=True)

class Vendor(models.Model):
    vendor_no = models.IntegerField(null=True)
    vendor_id = models.CharField(max_length=100, null=True, unique=True)
    vendor_name = models.CharField(max_length=100, null=True)
    vendor_address = models.CharField(max_length=200, null=True)
    vendor_mobile = models.CharField(max_length=15,null=True)
    
    def __str__(self):
            return self.vendor_id

class PurchaseOrder(models.Model):
    date = models.DateField(null=False)
    po_number = models.IntegerField(null=False)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)
    gross_amount = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    net_amount = models.IntegerField(null=True)
    
    def net_amount(self):
        return self.gross_amount - self.discount
    
class PurchasedItems(models.Model):
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,null=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    item_name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True, default=0)
    unit_price = models.IntegerField(null=True, default=0)
    total = models.IntegerField(null=True)
        
    def total(self):
        return self.quantity * self.unit_price
    
    # def item_name(self):
    #     if(self.item_id == Item.item_id):
    #         return Item.name
    #     return Item.name
       