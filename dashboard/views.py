from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Customer, Vendor, Item,MyUUIDModel,PurchasedItems, PurchaseOrder
from django.contrib.auth.models import User
from .forms import CustomerForm, PurchaseOrderForm, VendorForm, ItemForm,PurchasedItemForm
from django.contrib import messages
from django.db.models import Q, Max, F

# reort generation report lab
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#xhtmltopdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



# Create your views here.

@login_required
def index(request):
    
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    a = ["admin", "manager"]
    workers = User.objects.exclude(username__in = a)
    workers_count = workers.count()
    customer_count = Customer.objects.all().count()
    vendors = Vendor.objects.all()
    vendor_count = vendors.count()

    context = {
        'workers': workers,
        'workers_count': workers_count,
        'customer_count' : customer_count,
        'vendor_count' : vendor_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_delete(request, pk):
    workers = User.objects.get(id=pk)
    if request.method == 'POST':
        workers.delete()
        return redirect('dashboard-staff')
    context = {
        'workers' : workers,
    }
        
    return render(request, 'dashboard/staff_delete.html',context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    workers_count =  User.objects.all().count()
    context = {
        'workers': workers,
        'workers_count'  : workers_count,
    }
    return render(request, 'dashboard/staff_detail.html',context)

@login_required
def customer(request):
    customers = Customer.objects.all()
    customer_count = customers.count()
    workers = User.objects.exclude(username='admin')
    workers_count = workers.count()
    vendors = Vendor.objects.all()
    vendor_count = vendors.count()
    c_id = 101 if Customer.objects.count() == 0 else Customer.objects.aggregate(max=Max('customer_no'))["max"] + 1
    if request.method == 'POST':
        # cu_id = request.POST.get('cu_id')
        name = request.POST.get('customer_name')
        address = request.POST.get('customer_address')
        mob = request.POST.get('customer_mobile')
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer(customer_no=c_id,customer_id=(f'{"C"}{c_id}'),customer_name=name,customer_address=address,customer_mobile=mob).save()
            # redirect('dashboard/customer')
    else:
        form = CustomerForm()
    context = {
        'customers': customers,
        'workers' : workers,
        'workers_count' : workers_count,
        'customer_count' : customer_count,
        'vendor_count' : vendor_count,
        'form' : form,
    }
    return render(request, 'dashboard/customers.html', context)

# @login_required
# def customer_add(request):
#     return render(request, 'dashboard/customer_add.html')
    
@login_required
def customer_view(request, pk):
    customers = Customer.objects.get(id=pk)
    context = {
        'customers' : customers,
    }
    return render(request, 'dashboard/customer_view.html',context)

@login_required
def customer_delete(request, pk):
    customers = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('dashboard-customer')
    context = {
        'customers' : customers,
    }
    return render(request, 'dashboard/customer_delete.html',context)

@login_required
def vendor(request):
    vendors = Vendor.objects.all()
    vendor_count = vendors.count()
    workers = User.objects.exclude(username='admin')
    workers_count = workers.count()
    customer_count = Customer.objects.all().count()
    v_id = 101 if Vendor.objects.count() == 0 else Vendor.objects.aggregate(max=Max('vendor_no'))["max"] + 1
    if request.method == 'POST':
        # ve_id = request.POST.get('ve_id')
        name = request.POST.get('vendor_name')
        address = request.POST.get('vendor_address')
        mob = request.POST.get('vendor_mobile')
        form = VendorForm(request.POST)
        if form.is_valid():
            Vendor(vendor_no=v_id,vendor_id=(f'{"V"}{v_id}'),vendor_name=name,vendor_address=address,vendor_mobile=mob).save()
            # redirect('dashboard/vendor')


    else:
        form = VendorForm()
    context = {
        'form' : form,  
        'vendors': vendors,
        'vendor_count' : vendor_count,
        'workers_count': workers_count,
        'customer_count' : customer_count,
    }
    return render(request, 'dashboard/vendor.html',context)

@login_required
def vendor_view(request, pk):
    vendors = Vendor.objects.get(id=pk)
    context = {
        'vendors' : vendors,
    }
    return render(request, 'dashboard/vendor_veiw.html',context)

@login_required
def vendor_delete(request, pk):
    vendors = Vendor.objects.get(id=pk)
    if request.method == 'POST':
        vendors.delete()
        return redirect('dashboard-vendor')
    context = {
        'vendors' : vendors,
    }
    return render(request, 'dashboard/vendor_delete.html',context)

@login_required
def stock(request):
    items = Item.objects.all()
    p_id = 101 if Item.objects.count() == 0 else Item.objects.aggregate(max=Max('item_no'))["max"] + 1
    if request.method == 'POST':
    #     i_id = request.POST.get('i_id')
        price = request.POST.get('unit_price')
        name = request.POST.get('name')
        form = ItemForm(request.POST)
        if form.is_valid():
            Item(item_no=p_id,item_id=(f'{"P"}{p_id}'),name=name,unit_price=price).save()
            # form.save()
    else:
        form = ItemForm
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/stock.html',context)

@login_required
def purchase(request):
    vendors = Vendor.objects.all()
    purchase_orders = PurchaseOrder.objects.all()
    po_n = 101 if PurchaseOrder.objects.count() == 0 else PurchaseOrder.objects.aggregate(max=Max('po_no'))["max"] + 1
    if request.method == 'POST':
        # g_amount = request.POST.get('gross_amount')
        # dis = request.POST.get('discount')
        form = PurchaseOrderForm(request.POST)
        ven = request.POST.get('vendor_id')
        ven1 = vendors.get(id=ven)
        # ven1 = purchase_orders.get(id=ven)
        if form.is_valid():
            # form.save()
            PurchaseOrder(po_no=po_n,po_number=(f'{"PO"}{po_n}'),vendor_id=ven1).save()
            po = (f'{"PO"}{po_n}')
            # ven2 = purchase_orders.get(po_number=po)
            ven2 = purchase_orders.values('po_number').filter(po_number=po)[0]['po_number']
            return redirect("purchase_add" ,ven2)
    else:
        form = PurchaseOrderForm
    context = {
        'purchase_orders' : purchase_orders,
        'form' : form,
    }
    return render(request, 'purchase/purchase_orders.html',context)

@login_required
def purchase_add(request, po_number):
    vendors = Vendor.objects.all()
    items = Item.objects.all()
    purchase_orders = PurchaseOrder.objects.all()
    current_po_number = purchase_orders.values('po_number').filter(po_number=po_number)[0]['po_number']
    current_vendor_id = purchase_orders.values('vendor_id').filter(po_number=po_number)[0]['vendor_id']
    current_vendor_id1 = vendors.values('vendor_id').filter(id=current_vendor_id)[0]['vendor_id']
    # purchase_order = PurchaseOrder.objects.get(po_number=po_number)
    purchase_orders = PurchaseOrder.objects.all()
    purchased_items = PurchasedItems.objects.all()
    # not need
    # field_name = 'total_amount'
    # total1 = PurchasedItems._meta.get_field(field_name)
    # g_amount = 0 if total1 == 0 else PurchasedItems.objects.aggregate(max=Max('total_amount'))["max"] + 10
    # t_amount = PurchasedItems.quantity * PurchasedItems.unit_price
    # purchased_items = PurchasedItems.objects.annotate(t_amount = F('quantity') - F('unit_price'))
    # total_spent =  PurchasedItems.objects.filter(id=id).annotate(total_spent=(F('quantity') * F('unit_price')))
    # not need 
    if request.method == "POST":
        # not need
        # vendor = request.POST.get('vendor_id')
        # i_id = request.POST.get('item_id')
        # qty = request.POST.get('quantity')
        # u_price = request.POST.get('unit_price')
        # s = items.filter(name=i_name).values('item_id')
        # s = items.only('item_id').get(name=i_name).item_id
        # s = items.values('name').filter(item_id=i_id)[0]['name']
        # PurchasedItems.objects.create(item_id=items.get(item_id=i_id),item_name=s,vendor_id=vendors.get(vendor_id=vendor),quantity=qty,unit_price=u_price)
        # return redirect('purchase_add')
        # PurchaseOrder(gross_amount=g_amount).save()
        # PurchasedItems(total_amount=total_spent).save()
        # not need
        form = PurchasedItemForm(request.POST)
        i_id=request.POST['item_id']
        current_item_id = items.values('item_id').filter(id=i_id)[0]['item_id']
        qty=request.POST['quantity']
        uprice=request.POST['unit_price']
        if form.is_valid():
            # form.save()
            # return redirect('purchase_add', po_number)
            PurchasedItems(po_number=purchase_orders.get(po_number=current_po_number),item_id=items.get(item_id=current_item_id),vendor_id=vendors.get(id=current_vendor_id),quantity=qty,unit_price=uprice).save()
            return redirect('purchase_add', po_number)
        
    else:
        form = PurchasedItemForm

    context = { 
        'vendors': vendors,
        'items' : items,
        'purchased_items' : purchased_items,
        'form' : form,
        'purchase_orders':purchase_orders,
        'current_po_number' : current_po_number,
        'current_vendor_id1':current_vendor_id1
    } 
    return render(request, 'purchase/purchase_add.html',context)

@login_required
def purchaseditem_update(request, id):
    purchased_items = PurchasedItems.objects.get(pk=id)
    form = PurchasedItemForm(request.POST or None, instance = purchased_items)
    if form.is_valid():
        form.save()
        return redirect('purchaseditem_update',id)
    
    context = {
        'purchased_items' : purchased_items,
        'form' : form,
    }
    return render(request, 'purchase/purchaseditem_update.html',context)

@login_required
def purchaseditem_delete(request, id):
    purchased_items = PurchasedItems.objects.get(pk=id)
    if request.method == 'POST':
        purchased_items.delete()
        return redirect('purchaseditem_delete',id)
    context = {
        'purchased_items' : purchased_items,
    }
    return render(request, 'purchase/purchaseditem_delete.html',context)

# @login_required
# def addtocart(request):
#     if request.method == 'POST':
#         prod_id =  request.POST.get('product_id')
#         qty_input = request.POST.get('product_qty')
#         product_check = Item.objects.get(item_id=prod_id)
#         if (product_check):
#             PurchasedItems.objects.create(item_id=prod_id,quantity=qty_input)
#             return JsonResponse({'status':"added"})
#         else:
#             return JsonResponse({'status':"no such pro"})
#     return redirect('purchase_add')
        
        

@login_required
def demo(request):
    regno = 1 if MyUUIDModel.objects.count() == 0 else MyUUIDModel.objects.aggregate(max=Max('regnumber'))["max"] + 1
    if request.method == 'POST':
        regnumber = request.POST['regnumber']
        username = request.POST['username']
        MyUUIDModel(username=username,regnumber=regno,regnumber1=(f'{"V00"}{regno}')).save()
        
    return render(request, 'dashboard/uuid.html')
# @login_required
# def product(request): 
    # items = Product.objects.all()
    # workers = User.objects.exclude(username='admin')
    # product_count = items.count()
    # order_count = Order.objects.all().count()
    # # items = Product.objects.raw('SELECT * FROM dashboard_product')
    # workers_count = workers.count()

    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     items = Product.objects.filter(Q(name__icontains=q) | Q(category__icontains=q))
    # else:
    #     items = Product.objects.all()

    # # workers_count = workers.count()
    # if request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         product_name = form.cleaned_data.get('name')
    #         messages.success(request, f'{product_name} has been added')
    #         redirect('dashboard/product')
    # else:
    #     form = ProductForm()
    # context = {
    #     'items': items,
    #     'form': form,
    #     'product_count' : product_count,
    #     'workers_count' : workers_count,
    #     'order_count' : order_count,

    # }
    return render(request, 'dashboard/product.html')

@login_required
def product_delete(request, pk):
    # items = Product.objects.get(id=pk)
    # if request.method == 'POST':
    #     items.delete()
    #     return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_edit(request, pk):
    # items = Product.objects.get(id=pk)
    # if request.method == 'POST':
    #     form = ProductForm(request.POST, instance=items)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('dashboard-product')
    # else:
    #     form = ProductForm(instance=items)
    # context={
    #     'form' : form,
    # }
    return render(request, 'dashboard/product_edit.html')

# @login_required
# def product_add(request):


# @login_required
# def order(request):
#     customers = User.objects.all()
#     workers = User.objects.exclude(username='admin')
#     orders = Order.objects.all()
#     order_count = orders.count()
#     workers_count = workers.count()
#     product_count = Product.objects.all().count()
#     if 'q' in request.GET:
#         q = request.GET['q']
        # orders = Order.objects.get(Q(staff__icontains=q))
    # else:
    #     orders = Order.objects.all()


    # context = {
    #     'orders' : orders,
    #     'workers_count' : workers_count,
    #     'order_count' : order_count,
    #     'product_count' : product_count,
    #     'customers'  : customers,

    # }
    # return render(request, 'dashboard/order.html' ,context)

# @login_required
# def order_delete(request, pk):
#     items = Order.objects.get(id=pk)
#     if request.method == 'POST':
#         items.delete()
#         return redirect('dashboard-order')

#     return render(request, 'dashboard/order_delete.html' )

# @login_required
# def staff_order_delete(request, pk):
#     items = Order.objects.get(id=pk)
#     if request.method == 'POST':
#         items.delete()
        # return redirect('dashboard-index')

    # return render(request, 'dashboard/staff_order_delete.html' )
#xhtml2pdf

@login_required
def report_pdf(request):
    items = Product.objects.all()
    template_path = 'dashboard/product_pdf.html'
    context = {'items': items}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




