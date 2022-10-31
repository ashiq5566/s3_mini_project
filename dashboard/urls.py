from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.index, name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff/delete/<int:pk>',views.staff_delete,name='dashboard-staff-delete'),
    path('staff/detail/<int:pk>',views.staff_detail,name='dashboard-staff-detail'),
    path('customer/',views.customer,name='dashboard-customer'),
    path('customer/view/<int:pk>',views.customer_view,name='dashboard-customer-view'),
    path('customer/delete/<int:pk>',views.customer_delete,name='dashboard-customer-delete'),
    path('vendor/',views.vendor,name='dashboard-vendor'),
    path('vendor/view/<int:pk>',views.vendor_view,name='dashboard-vendor-view'),
    path('vendor/delete/<int:pk>',views.vendor_delete,name='dashboard-vendor-delete'),
    path('stock/',views.stock,name='stock'),
    path('stock/update/<int:pk>',views.stock_update,name='stock_update'),
    path('purchase/',views.purchase,name='purchase'),
    path('purchase/view/<int:pk>',views.purchase_view,name='purchase_view'),
    path('purchase/view/<int:pk>/pdf',views.report_pdf,name='report_pdf'),
    path('purchase/add/<po_number>',views.purchase_add,name='purchase_add'),
    path('purchase/add/<po_number>/confirm',views.purchase_add_confirm,name='purchase_add_confirm'),
    # path('purchase/add/<po_number>/purchaseditem_update/<int:id>',views.purchaseditem_update,name='purchaseditem_update'),
    path('purchase/add/<po_number>/purchaseditem_delete/<int:id>',views.purchaseditem_delete,name='purchaseditem_delete'),
    path('payment/',views.payment,name='payment'),
    path('payment/<vendor_id>',views.payment_vendor,name='payment_vendor'),
    path('payment/<vendor_id>/<int:pk>',views.payment_purchase_order,name='payment_purchase_order'),
    path('purchase/return',views.purchase_return,name='purchase_return'),
    path('purchase/return/<po_number>',views.purchase_return_po,name='purchase_return_po'),
    
    
    path('demo/',views.demo,name='demo'),
    path('sales/',views.sales,name='sales'),
    path('sales/view/<int:pk>',views.sales_view,name='sales_view'),
    path('sales/view/<int:pk>/pdf',views.sales_report_pdf,name='sales_report_pdf'),
    path('sales/add/<so_number>',views.sales_add,name='sales_add'),
    path('sales/add/<so_number>/confirm',views.sales_add_confirm,name='sales_add_confirm'),
    path('sales/add/<so_number>/solditem_delete/<int:id>',views.solditem_delete,name='solditem_delete'),
    path('sales/payment/',views.sales_payment,name='sales_payment'),
    path('sales/payment/<customer_id>',views.payment_customer,name='payment_customer'),
    path('sales/payment/<customer_id>/<int:pk>',views.payment_sales_order,name='payment_sales_order'),
]

