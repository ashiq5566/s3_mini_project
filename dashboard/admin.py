from django.contrib import admin
from .models import Customer, PurchaseReturn, Vendor, Item, MyUUIDModel,PurchasedItems, PurchaseOrder, Payment, SalesOrder, SoldItems

admin.site.site_header = "Inventory Management System"

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','customer_name', 'customer_address','customer_mobile')

class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id','vendor_name', 'vendor_address','vendor_mobile')
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id','name','unit_price','qty_purchased','qty_sold','status')

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('date','po_number','vendor_name','gross_amount','discount','net_amount','status')
        
class PurchasedItemsAdmin(admin.ModelAdmin):
    list_display = ('id','po_number','vendor_id','item_id','item_name','quantity','unit_price','total_amt')
    
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('date','so_number','customer_name','gross_amount','discount','net_amount','status')
        
class SoldItemsAdmin(admin.ModelAdmin):
    list_display = ('id','so_number','customer_id','item_id','item_name','quantity','unit_price','total_amt')
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id','po_number','paid','pending','total')

class PurchaseReturnAdmin(admin.ModelAdmin):
    list_display = ('po_number','item_name','return_qty','amount')

class MyUUIDModelAdmin(admin.ModelAdmin):
    list_display = ('regnumber1','username')


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product','staff','order_quantity','u_price','total_order_price','date')
#     list_filter = ['product','staff']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(PurchasedItems, PurchasedItemsAdmin)
admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(SoldItems, SoldItemsAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PurchaseReturn, PurchaseReturnAdmin)
admin.site.register(MyUUIDModel, MyUUIDModelAdmin)


