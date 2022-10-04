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
    path('purchase/add/',views.purchase_add,name='purchase_add'),
    path('purchase/add/purchaseditem_update/<id>',views.purchaseditem_update,name='purchaseditem_update'),
    path('purchase/add/purchaseditem_delete/<int:pk>',views.purchaseditem_delete,name='purchaseditem_delete'),
    # path('purchase/add/cart/',views.addtocart,name='add-to-cart'),

    path('demo/',views.demo,name='demo'),
]

