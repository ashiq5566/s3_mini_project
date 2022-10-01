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
        name = models.CharField(max_length=100, null=True)
        unit_price = models.PositiveBigIntegerField(null=True)
        qty_available = models.PositiveIntegerField(null=True, default=0)
        qty_sold = models.PositiveIntegerField(null=True, default=0)
        status = models.BooleanField(default=False)
     
    
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