from django.contrib import admin
from .models import Customer, Vendor, Item, MyUUIDModel

admin.site.site_header = "Inventory Management System"

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','customer_name', 'customer_address','customer_mobile')

class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id','vendor_name', 'vendor_address','vendor_mobile')
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id','name','unit_price','qty_available','qty_sold','status')

class MyUUIDModelAdmin(admin.ModelAdmin):
    list_display = ('regnumber1','username')


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product','staff','order_quantity','u_price','total_order_price','date')
#     list_filter = ['product','staff']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MyUUIDModel, MyUUIDModelAdmin)

