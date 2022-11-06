from email.policy import default
from enum import unique
from pyexpat import model
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
        name = models.CharField(max_length=100, null=True, blank=False,unique=True)
        unit_price = models.PositiveBigIntegerField(null=True,blank=True)
        qty_available = models.PositiveIntegerField(null=True, default=0)
        qty_sold = models.PositiveIntegerField(null=True, default=0)
        qty_purchased = models.PositiveIntegerField(null=True, default=0)
        status = models.BooleanField(default=False)
        
        def __str__(self):
            return  self.name
     
    
class Customer(models.Model):
    customer_no = models.IntegerField(null=True)
    customer_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    customer_name = models.CharField(max_length=100,null=True)
    customer_address = models.CharField(max_length=200,null=True)
    customer_mobile = models.CharField(max_length=15,null=True)
    
    def __str__(self):
            return self.customer_name

class Vendor(models.Model):
    vendor_no = models.IntegerField(null=True)
    vendor_id = models.CharField(max_length=100, null=True, unique=True)
    vendor_name = models.CharField(max_length=100, null=True)
    vendor_address = models.CharField(max_length=200, null=True)
    vendor_mobile = models.CharField(max_length=15,null=True)
    
    def __str__(self):
            return self.vendor_name

class PurchaseOrder(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    po_no = models.IntegerField(null=True)
    po_number = models.CharField(max_length=100, null=True, unique=True)
    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)
    gross_amount = models.PositiveIntegerField(null=True)
    discount = models.PositiveIntegerField(null=True)
    net_amount = models.PositiveIntegerField(null=True)
    net_pending = models.PositiveIntegerField(null=True,default=0)
    status = models.BooleanField(default=False,null=True)
    
    def __str__(self):
            return self.po_number
    
    # def save(self, *args, **kwargs):
    #     self.net_amount = int(self.gross_amount) - int(self.discount)
    #     super(PurchaseOrder, self).save(*args, **kwargs)
    
class PurchasedItems(models.Model):
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,null=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)
    item_id = models.CharField(max_length = 20,null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(null=True, default=0)
    unit_price = models.PositiveIntegerField(null=True, default=0)
    total_amt = models.PositiveIntegerField(null=True)

        
    def save(self, *args, **kwargs):
        self.total_amt = int(self.quantity) * int(self.unit_price)
        super(PurchasedItems, self).save(*args, **kwargs) 
    # def save(self):
    #     total_amt = self.quantity * self.unit_price
    #     return total_amt
    @property   
    def item_id(self):
        return self.item_name.item_id
    
class SalesOrder(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    so_no = models.IntegerField(null=True)
    so_number = models.CharField(max_length=100, null=True, unique=True)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    gross_amount = models.PositiveIntegerField(null=True)
    discount = models.PositiveIntegerField(null=True)
    net_amount = models.PositiveIntegerField(null=True)
    net_pending = models.PositiveIntegerField(null=True,default=0)
    status = models.BooleanField(default=False,null=True)
    
    def __str__(self):
            return self.so_number
        

class SoldItems(models.Model):
    so_number = models.ForeignKey(SalesOrder, on_delete=models.CASCADE,null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    item_id = models.CharField(max_length = 20,null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(null=True, default=0)
    unit_price = models.PositiveIntegerField(null=True, default=0)
    total_amt = models.PositiveIntegerField(null=True)

        
    def save(self, *args, **kwargs):
        self.total_amt = int(self.quantity) * int(self.unit_price)
        super(SoldItems, self).save(*args, **kwargs) 
    
    
    @property
    def item_id(self):
        return self.item_name.item_id
            
class Payment(models.Model):
    date = models.DateTimeField(auto_now_add=True,null=True)
    payment_no = models.IntegerField(null=True)
    payment_id = models.CharField(max_length=100, null=True, unique=True)
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(null=True,default=0)
    total = models.PositiveIntegerField(null=True)
    pending = models.PositiveIntegerField(null=True,default=0)

class PaymentSales(models.Model):
    date = models.DateTimeField(auto_now_add=True,null=True)
    payment_no = models.IntegerField(null=True)
    payment_id = models.CharField(max_length=100, null=True, unique=True)
    so_number = models.ForeignKey(SalesOrder, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(null=True,default=0)
    total = models.PositiveIntegerField(null=True)
    pending = models.PositiveIntegerField(null=True,default=0)
    
class PurchaseReturn(models.Model):
    date = models.DateTimeField(auto_now_add=True,null=True)
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    return_qty = models.PositiveIntegerField(null=True,default=0)
    amount = models.PositiveIntegerField(null=True)
    
class SalesReturn(models.Model):
    date = models.DateTimeField(auto_now_add=True,null=True)
    so_number = models.ForeignKey(SalesOrder, on_delete=models.CASCADE,null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    return_qty = models.PositiveIntegerField(null=True,default=0)
    amount = models.PositiveIntegerField(null=True)

