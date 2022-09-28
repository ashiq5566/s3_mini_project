import uuid
from django.db import models
# from dashboard.views import product
from django.contrib.auth.models import User

# Create your models here.   
class Item(models.Model):
        item_id = models.CharField(max_length=10,null=True, unique=True)
        name = models.CharField(max_length=100, null=True)
        unit_price = models.PositiveBigIntegerField(null=True)
        qty_available = models.PositiveIntegerField(null=True, default=0)
        qty_sold = models.PositiveIntegerField(null=True, default=0)
        status = models.BooleanField(default=False)
    
    
class Customer(models.Model):
    customer_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    customer_name = models.CharField(max_length=100,null=True)
    customer_address = models.CharField(max_length=200,null=True)
    customer_mobile = models.CharField(max_length=15,null=True)

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=100, null=True, unique=True)
    vendor_name = models.CharField(max_length=100, null=True)
    vendor_address = models.CharField(max_length=200, null=True)
    vendor_mobile = models.CharField(max_length=15,null=True)