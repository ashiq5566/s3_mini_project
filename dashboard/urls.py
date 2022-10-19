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
    path('purchase/',views.purchase,name='purchase'),
    path('purchase/view/<int:pk>',views.purchase_view,name='purchase_view'),
    path('purchase/view/<int:pk>/pdf',views.report_pdf,name='report_pdf'),
    path('purchase/add/<po_number>',views.purchase_add,name='purchase_add'),
    path('purchase/add/<po_number>/confirm',views.purchase_add_confirm,name='purchase_add_confirm'),
    # path('purchase/add/<po_number>/purchaseditem_update/<int:id>',views.purchaseditem_update,name='purchaseditem_update'),
    path('purchase/add/<po_number>/purchaseditem_delete/<int:id>',views.purchaseditem_delete,name='purchaseditem_delete'),
    path('payment/',views.payment,name='payment'),
    path('payment/<vendor_id>',views.payment_vendor,name='payment_vendor'),
    path('demo/',views.demo,name='demo'),
]

