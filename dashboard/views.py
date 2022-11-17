from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Customer, SalesOrder, Vendor, Item,MyUUIDModel,PurchasedItems, PurchaseOrder, Payment,SoldItems,PaymentSales, PurchaseReturn, SalesReturn
from django.contrib.auth.models import User
from .forms import CustomerForm, PurchaseOrderForm, VendorForm, ItemForm,PurchasedItemForm, SelectVendorForm,SalesOrderForm, SoldItemForm, SelectCustomerForm, SelectPOForm, SelectSOForm
from django.contrib import messages
from django.db.models import Q, Max, F, Sum

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
from django.db.models.functions import TruncMonth
from django.db.models import Count



# Create your views here.

@login_required
def index(request):
    items = Item.objects.all()
    # sales_report=SalesOrder.objects.annotate(month=TruncMonth('date')).values('month').annotate(c=Count('id')).values('month', 'c')                    
    # print(sales_report)
    # report = SalesOrder.objects.filter(recordDate__gte='2019-03-01', recordDate__lte='2019-03-09')

    
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/index.html',context)


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
def customer_update(request, pk):
    customers = Customer.objects.get(id=pk)
    form = CustomerForm(request.POST or None, instance = customers)
    if form.is_valid():
            form.save()
            return redirect("dashboard-customer")
    context = {
        'form' : form
    }
    return render(request, 'dashboard/customer_update.html',context)


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
def vendor_update(request, pk):
    vendors = Vendor.objects.get(id=pk)
    form = VendorForm(request.POST or None, instance = vendors)
    if form.is_valid():
            form.save()
            return redirect("dashboard-vendor")
    context = {
        'form' : form
    }
    return render(request, 'dashboard/vendor_update.html',context)

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
        #i_id = request.POST.get('i_id')
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
def stock_update(request, pk):
    items = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance = items)
    if form.is_valid():
            form.save()
            return redirect("stock")
    
    context = {
        'form' : form
    }
    return render(request, 'dashboard/stock_update.html',context)

@login_required
def purchase(request):
    vendors = Vendor.objects.all()
    purchase_orders_new = PurchaseOrder.objects.all()
    purchase_orders = PurchaseOrder.objects.all().exclude(gross_amount=None)
    po_n = 101 if PurchaseOrder.objects.count() == 0 else PurchaseOrder.objects.aggregate(max=Max('po_no'))["max"] + 1
    if request.method == 'POST':
        # g_amount = request.POST.get('gross_amount')
        # dis = request.POST.get('discount')    
        form = PurchaseOrderForm(request.POST)
        ven = request.POST.get('vendor_name')
        ven1 = vendors.get(id=ven)
        # ven1 = purchase_orders.get(id=ven)
        if form.is_valid():
            # form.save()
            PurchaseOrder(po_no=po_n,po_number=(f'{"PO"}{po_n}'),vendor_name=ven1).save()
            po = (f'{"PO"}{po_n}')
            # ven2 = purchase_orders.get(po_number=po)
            ven2 = purchase_orders_new.values('po_number').filter(po_number=po)[0]['po_number']
            return redirect("purchase_add" ,ven2)
    else:
        form = PurchaseOrderForm
    context = {
        'purchase_orders' : purchase_orders,
        'form' : form,
    }
    return render(request, 'purchase/purchase_orders.html',context)
@login_required
def purchase_view(request, pk):
    purchase_orders = PurchaseOrder.objects.get(id=pk)
    purchase_orders1 = PurchaseOrder.objects.all()
    current_po_number = purchase_orders1.values('id').filter(id=pk)[0]['id']
    purchase_order_views = PurchasedItems.objects.filter(po_number_id=current_po_number)
    current_purchase_orderid = PurchaseOrder.objects.get(id=pk).id
    current_po = PurchaseOrder.objects.get(id=current_po_number).po_number
    current_vendor = PurchaseOrder.objects.get(id=current_po_number).vendor_name
    current_vendor_name = Vendor.objects.get(vendor_name=current_vendor).vendor_name
    current_vendor_id = Vendor.objects.get(vendor_name=current_vendor).vendor_id
    po_date = PurchaseOrder.objects.get(id=current_po_number).date
    discount = PurchaseOrder.objects.get(id=current_po_number).discount
    # net_amt = PurchaseOrder.objects.get(id=current_po_number).net_amount
       
    total_amt = 0
    _id = PurchaseOrder.objects.get(id=pk).id
    for each in PurchasedItems.objects.filter(po_number__id=_id):
        total_amt += each.total_amt
    net = int(total_amt) - int(discount)
    context = {
        'purchase_orders' : purchase_orders,
        'purchase_order_views' : purchase_order_views,
        'total_amt' : total_amt,
        'discount' : discount,
        'net' : net,
        'current_purchase_orderid' : current_purchase_orderid,
        'current_po' : current_po,
        'current_vendor' : current_vendor,
        'po_date' : po_date,
        'current_vendor_name' : current_vendor_name,
        'current_vendor_id' : current_vendor_id
    }
    return render(request, 'purchase/purchase_view.html',context)

@login_required
def purchase_add(request, po_number):
    vendors = Vendor.objects.all()
    items = Item.objects.all()
    purchase_orders = PurchaseOrder.objects.all()
    current_po_number = purchase_orders.values('po_number').filter(po_number=po_number)[0]['po_number']
    current_vendor_id = purchase_orders.values('vendor_name').filter(po_number=po_number)[0]['vendor_name']
    current_vendor_id1 = vendors.values('vendor_id').filter(id=current_vendor_id)[0]['vendor_id']
    purchase_orders = PurchaseOrder.objects.all()
    purchased_items = PurchasedItems.objects.all()
    current_po_number_view = purchase_orders.values('id').filter(po_number=po_number)[0]['id']
    purchase_order_individals = PurchasedItems.objects.filter(po_number_id=current_po_number_view)
    
    po_id = PurchaseOrder.objects.get(po_number=current_po_number).id
    p_items = PurchasedItems.objects.filter(po_number_id=po_id)
    p_lists = p_items.values_list('item_name', flat=True)
    print('p_lists' ,p_lists)
    
    total_amt = 0
    _id = PurchaseOrder.objects.get(po_number=po_number).id
    for each in PurchasedItems.objects.filter(po_number__id=_id):
        total_amt += each.total_amt
    # print("TOTAL:", total_amt) 
    # print("LOGGGG:", _id)  
    
    if request.method == "POST":  
        form = PurchasedItemForm(request.POST)
        i_name=request.POST['item_name']
        current_item_id = items.values('item_id').filter(id=i_name)[0]['item_id']
        qty=int(request.POST['quantity'])
        uprice=int(request.POST['unit_price'])
        g_amount = request.POST.get('g_amount')
        record = Item.objects.get(id=i_name)    
        record.qty_purchased = record.qty_purchased + qty
        item_id = Item.objects.get(item_id=current_item_id).id
        print("dfdff",i_name) 
        print(item_id)
        if form.is_valid():
            if item_id in p_lists:     
                return redirect('error_404')
            else: 
                PurchasedItems(po_number=purchase_orders.get(po_number=current_po_number),item_name=items.get(item_id=current_item_id),vendor_id=vendors.get(id=current_vendor_id),quantity=qty,unit_price=uprice).save()
                record.save()
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
        'current_vendor_id1':current_vendor_id1,
        'purchase_order_individals':purchase_order_individals,
        'total_amt':  total_amt,
        # 'each_total_amount':each_total_amount
    } 
    return render(request, 'purchase/purchase_add.html',context)

@login_required
def purchase_add_confirm(request ,po_number):
    # purchase_orders = PurchaseOrder.objects.get(pk=po_number) 
    purchase_orders = PurchaseOrder.objects.all()
    current_po_number = purchase_orders.values('po_number').filter(po_number=po_number)[0]['po_number']
    current_po_number_view = purchase_orders.values('id').filter(po_number=po_number)[0]['id']
    purchase_order_individals = PurchasedItems.objects.filter(po_number_id=current_po_number_view)
    
    total_amt = 0
    _id = PurchaseOrder.objects.get(po_number=po_number).id
    for each in PurchasedItems.objects.filter(po_number__id=_id):
        total_amt += each.total_amt
    if request.method == "POST":
        g = request.POST.get('g_amount')
        d = request.POST.get('discount')
        record = PurchaseOrder.objects.get(po_number=current_po_number)
        record.gross_amount = g
        record.discount = d
        net = int(g) - int(d)
        record.net_amount = net
        record.net_pending = net
        record.save()
        return redirect('purchase')
    
    context = {
        'total_amt' : total_amt,
        'purchase_order_individals':purchase_order_individals,
        'current_po_number' : current_po_number
        
    }
    return render(request, 'purchase/purchase_confirm.html',context)

@login_required
def purchaseditem_delete(request, id, po_number):
    items = Item.objects.all()
    purchased_items = PurchasedItems.objects.get(pk=id)
    record = PurchasedItems.objects.get(pk=id).item_id
    qty = PurchasedItems.objects.get(pk=id).quantity
    stock = Item.objects.get(item_id=record)
    print("gello", qty)
    if request.method == 'POST':
        purchased_items.delete()
        stock.qty_purchased = stock.qty_purchased - qty
        stock.save()
        
        return redirect('purchase_add',po_number)
    context = {
        'purchased_items' : purchased_items,
    }
    return render(request, 'purchase/purchaseditem_delete.html',context)

@login_required
def report_pdf(request, pk):
    vendors = Vendor.objects.all()
    purchase_orders = PurchaseOrder.objects.all()
    purchase_orders = PurchaseOrder.objects.get(id=pk)
    purchase_orders1 = PurchaseOrder.objects.all()
    current_po_id = purchase_orders1.values('id').filter(id=pk)[0]['id']
    purchase_order_views = PurchasedItems.objects.filter(po_number_id=current_po_id)
    current_po_no = PurchaseOrder.objects.get(id=current_po_id).po_number
    current_vendor_id = PurchaseOrder.objects.get(id=current_po_id).vendor_name
    print_date = PurchaseOrder.objects.get(id=current_po_id).date
    discount = PurchaseOrder.objects.get(id=current_po_id).discount
    net_amt = PurchaseOrder.objects.get(id=current_po_id).net_amount
    total_amt = 0
    _id = PurchaseOrder.objects.get(id=pk).id
    for each in PurchasedItems.objects.filter(po_number__id=_id):
        total_amt += each.total_amt
    template_path = 'pdf/purchase_order_pdf.html'
    context = {
        'current_po_id' : current_po_id,
        'print_date' : print_date,
        'purchase_order_views' : purchase_order_views,
        'discount' : discount,
        'net_amt'  : net_amt,
        'total_amt' : total_amt,
        'current_po_no' : current_po_no,
        'current_vendor_id' : current_vendor_id
        
        
    }
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

  
def payment(request):
    vendors = Vendor.objects.all()
    if request.method == "POST":  
        form = SelectVendorForm(request.POST)
        v = request.POST.get('vendor_id')
        v_id = Vendor.objects.get(id=v).vendor_id
        print("gwgw" ,v_id)
        return redirect('payment_vendor', v_id)
        

    else:
        form = SelectVendorForm()
    # if request.method == 'POST':
    #     v = request.POST.get('v_id')
    context = {
        "vendors" : vendors,
        "form" : form
    }
    return render(request, 'payment/payment_add.html',context)
  
@login_required
def purchase_return(request):
    if request.method == "POST":
        form = SelectPOForm(request.POST)
        po = request.POST.get('PurchaseOrderID')
        current_po = PurchaseOrder.objects.get(id=po)
        print("gwgw" ,po)
        return redirect('purchase_return_po',current_po)
    else:
        form = SelectPOForm()
    context = {
        'form' : form,
    }
        
    return render(request, 'purchaseReturn/purchase_return.html',context)    

@login_required
def purchase_return_po(request,po_number):
    items = Item.objects.all()
    current_po = po_number
    pn_id = PurchaseOrder.objects.get(po_number=po_number).id 
    purchased_items = PurchasedItems.objects.filter(po_number_id = pn_id)
    
    if request.method == "POST":
        item_name = request.POST.get('i_name')
        re_qty = request.POST.get('rq')
        inm = Item.objects.get(name=item_name).id
        unit_price = PurchasedItems.objects.get(po_number_id = pn_id , item_name=inm).unit_price
        amt = int(re_qty) * int(unit_price)
        PurchaseReturn(po_number=PurchaseOrder.objects.get(po_number=current_po),item_name = items.get(name=item_name),return_qty = re_qty,amount=amt).save()
        record = Item.objects.get(id=inm)
        if int(re_qty) <= int(record.qty_purchased):
            record.qty_purchased = int(record.qty_purchased) - int(re_qty)
            record.save()
            record2 = PurchaseOrder.objects.get(po_number=current_po)
            record2.net_amount = int(record2.net_amount) - int(amt)
            record2.net_pending = int(record2.net_pending) - int(amt)
            record2.save()
        else:
            return redirect('error_404')
        
        return redirect('purchase_return_po', current_po)
        
    
    purchase_returns = PurchaseReturn.objects.filter(po_number_id=pn_id)
    
        
    
    context = {
        'purchased_items' : purchased_items,
        'current_po' : current_po,
        'purchase_returns' : purchase_returns
    }
        
    return render(request, 'purchaseReturn/purchase_return_po.html',context) 


@login_required
def payment_vendor(request, vendor_id):
    vid = Vendor.objects.get(vendor_id=vendor_id).id
    current_vendor_id = Vendor.objects.get(id=vid).vendor_id
    current_vendor_name = Vendor.objects.get(id=vid).vendor_name
    purchase_orders = PurchaseOrder.objects.filter(vendor_name = vid).exclude(gross_amount=None)
    # po_id = PurchaseOrder.objects.get()
    
    context = {
        "current_vendor_id" : current_vendor_id,
        "current_vendor_name" : current_vendor_name,
        "purchase_orders" : purchase_orders,
    }
    return render(request, 'payment/payment_vendor.html',context)     

@login_required
def payment_purchase_order(request,vendor_id, pk):
    purchase_orders = PurchaseOrder.objects.get(id=pk)
    purchase_orders1 = PurchaseOrder.objects.all()
    current_po = PurchaseOrder.objects.get(id=pk).po_number
    current_ve = PurchaseOrder.objects.get(id=pk).vendor_name
    current_id = PurchaseOrder.objects.get(id=pk).id
    net_total = PurchaseOrder.objects.get(id=pk).net_amount
    pending_amt = PurchaseOrder.objects.get(po_number=current_po).net_pending
    status = PurchaseOrder.objects.get(po_number=current_po).status
    
    payment_no = 101 if Payment.objects.count() == 0 else Payment.objects.aggregate(max=Max('payment_no'))["max"] + 1
    
    pending = PurchaseOrder.objects.get(id=pk).net_amount
    if request.method == "POST":
        paid_amt = request.POST.get('paid')
        
        if int(paid_amt) <= int(pending_amt):
            Payment(payment_no=payment_no,payment_id=(f'{"TNR"}{payment_no}'),po_number=purchase_orders1.get(po_number=current_po),paid=paid_amt).save()
            for each in Payment.objects.filter(po_number__id=pk):
                    pending -= each.paid
            record = PurchaseOrder.objects.get(po_number=current_po)
            record.net_pending = pending
            record.save()
        else:
            return redirect('error_payment')
        return redirect('payment_purchase_order',current_ve,current_id)
    payments = Payment.objects.filter(po_number_id=current_id)
    if pending_amt == 0:
        stat = PurchaseOrder.objects.get(po_number=current_po)
        stat.status = True
        stat.save()
        
    context = {
        "purchase_orders" : purchase_orders,
        "current_po" : current_po,
        "net_total" : net_total,
        # "pending" : pending,
        "payments" : payments
    }
    return render(request, 'payment/payment_purchase_order.html',context)   


@login_required
def sales(request):
    customers = Customer.objects.all()
    sales_orders_new = SalesOrder.objects.all()
    sales_orders = SalesOrder.objects.all().exclude(gross_amount=None)
    so_n = 101 if SalesOrder.objects.count() == 0 else SalesOrder.objects.aggregate(max=Max('so_no'))["max"] + 1
    if request.method == 'POST':  
        form = SalesOrderForm(request.POST)
        cus = request.POST.get('customer_name')
        cus1 = customers.get(id=cus)
        if form.is_valid():
            SalesOrder(so_no=so_n,so_number=(f'{"SO"}{so_n}'),customer_name=cus1).save()
            po = (f'{"SO"}{so_n}')
            cus2 = sales_orders_new.values('so_number').filter(so_number=po)[0]['so_number']
            return redirect("sales_add" ,cus2)
    else:
        form = SalesOrderForm
    context = {
        'sales_orders' : sales_orders,
        'form' : form,
    }
    return render(request, 'sales/sales_orders.html',context)

@login_required
def sales_add(request, so_number):
    customers = Customer.objects.all()
    items = Item.objects.all()
    sales_orders = SalesOrder.objects.all()
    current_so_number = sales_orders.values('so_number').filter(so_number=so_number)[0]['so_number']
    current_customer_id = sales_orders.values('customer_name').filter(so_number=so_number)[0]['customer_name']
    current_customer_id1 = customers.values('customer_id').filter(id=current_customer_id)[0]['customer_id']
    sales_orders = SalesOrder.objects.all()
    sold_items = SoldItems.objects.all()
    current_so_number_view = sales_orders.values('id').filter(so_number=so_number)[0]['id']
    sales_order_individals = SoldItems.objects.filter(so_number_id=current_so_number_view)
    
    so_id = SalesOrder.objects.get(so_number=current_so_number).id
    p_items = SoldItems.objects.filter(so_number_id=so_id)
    p_lists = p_items.values_list('item_name', flat=True)
    
    total_amt = 0
    _id = SalesOrder.objects.get(so_number=so_number).id
    for each in SoldItems.objects.filter(so_number__id=_id):
        total_amt += each.total_amt
    # print("TOTAL:", total_amt) 
    # print("LOGGGG:", _id)  
    
    if request.method == "POST":  
        form = SoldItemForm(request.POST)
        i_name=request.POST['item_name']
        current_item_id = items.values('item_id').filter(id=i_name)[0]['item_id']
        qty=int(request.POST['quantity'])
        # uprice=int(request.POST['unit_price'])
        uprice = Item.objects.get(item_id=current_item_id).unit_price
        g_amount = request.POST.get('g_amount')
        record = Item.objects.get(id=i_name)    
        print("sdsd", i_name)
        record.qty_sold = record.qty_sold + qty
        record.qty_purchased = int(record.qty_purchased) - int(record.qty_sold)
        item_id = Item.objects.get(item_id=current_item_id).id
        if form.is_valid():
            if item_id in p_lists or int(qty) > int(record.qty_purchased):     
                return redirect('error_404')
            else:
                SoldItems(so_number=sales_orders.get(so_number=current_so_number),item_name=items.get(item_id=current_item_id),customer_id=customers.get(id=current_customer_id),quantity=qty,unit_price=uprice).save()
                record.save()
                return redirect('sales_add', so_number)
            # form.save()
            # return redirect('purchase_add', so_number)
            
        
    else:
        form = SoldItemForm
    

    context = { 
        'customers': customers,
        'items' : items,
        'sold_items' : sold_items,
        'form' : form,
        'sales_orders':sales_orders,
        'current_so_number' : current_so_number,
        'current_customer_id1':current_customer_id1,
        'sales_order_individals':sales_order_individals,
        'total_amt':  total_amt,
        # 'item_id' : item_id,
        'p_lists' : p_lists
        # 'each_total_amount':each_total_amount
    } 
    return render(request, 'sales/sales_add.html',context)

@login_required
def sales_add_confirm(request ,so_number):
    # purchase_orders = PurchaseOrder.objects.get(pk=po_number) 
    sales_orders = SalesOrder.objects.all()
    current_so_number = sales_orders.values('so_number').filter(so_number=so_number)[0]['so_number']
    current_so_number_view = sales_orders.values('id').filter(so_number=so_number)[0]['id']
    sales_order_individals = SoldItems.objects.filter(so_number_id=current_so_number_view)
    
    total_amt = 0
    _id = SalesOrder.objects.get(so_number=so_number).id
    for each in SoldItems.objects.filter(so_number__id=_id):
        total_amt += each.total_amt
    if request.method == "POST":
        g = request.POST.get('g_amount')
        d = request.POST.get('discount')
        record = SalesOrder.objects.get(so_number=current_so_number)
        record.gross_amount = g
        record.discount = d
        net = int(g) - int(d)
        record.net_amount = net
        record.net_pending = net
        record.save()
        return redirect('sales')
    
    context = {
        'total_amt' : total_amt,
        'sales_order_individals':sales_order_individals,
        'current_so_number' : current_so_number
        
    }
    return render(request, 'sales/sales_confirm.html',context)

@login_required
def solditem_delete(request, id, so_number):
    items = Item.objects.all()
    sales_items = SoldItems.objects.get(pk=id)
    record = SoldItems.objects.get(pk=id).item_id
    qty = SoldItems.objects.get(pk=id).quantity
    stock = Item.objects.get(item_id=record)
    print("gello", qty)
    if request.method == 'POST':
        sales_items.delete()
        stock.qty_sold = stock.qty_sold - qty
        stock.qty_purchased = int(stock.qty_purchased) + int(qty)
        stock.save()
        
        return redirect('sales_add',so_number)
    context = {
        'sales_items' : sales_items,
    }
    return render(request, 'sales/solditem_delete.html',context)

@login_required
def sales_view(request, pk):
    sales_orders = SalesOrder.objects.get(id=pk)
    sales_orders1 = SalesOrder.objects.all()
    current_so_number = sales_orders1.values('id').filter(id=pk)[0]['id']
    sales_order_views = SoldItems.objects.filter(so_number_id=current_so_number)
    current_sales_orderid = SalesOrder.objects.get(id=pk).id
    current_so = SalesOrder.objects.get(id=current_so_number).so_number
    current_customer = SalesOrder.objects.get(id=current_so_number).customer_name
    current_customer_name = Customer.objects.get(customer_name=current_customer).customer_name
    current_customer_id = Customer.objects.get(customer_name=current_customer).customer_id
    so_date = SalesOrder.objects.get(id=current_so_number).date
    discount = SalesOrder.objects.get(id=current_so_number).discount
    net_amt = SalesOrder.objects.get(id=current_so_number).net_amount
    
    total_amt = 0
    _id = SalesOrder.objects.get(id=pk).id
    for each in SoldItems.objects.filter(so_number__id=_id):
        total_amt += each.total_amt
    context = {
        'sales_orders' : sales_orders,
        'sales_order_views' : sales_order_views,
        'total_amt' : total_amt,
        'discount' : discount,
        'net_amt' : net_amt,
        'current_sales_orderid' : current_sales_orderid,
        'current_so' : current_so,
        'current_customer' : current_customer,
        'so_date' : so_date,
        'current_customer_name' : current_customer_name,
        'current_customer_id' : current_customer_id
    }
    return render(request, 'sales/sales_view.html',context)

@login_required
def sales_report_pdf(request, pk):
    customers = Customer.objects.all()
    sales_orders = SalesOrder.objects.all()
    sales_orders = SalesOrder.objects.get(id=pk)
    sales_orders1 = SalesOrder.objects.all()
    current_so_id = sales_orders1.values('id').filter(id=pk)[0]['id']
    sales_order_views = SoldItems.objects.filter(so_number_id=current_so_id)
    current_so_no = SalesOrder.objects.get(id=current_so_id).so_number
    current_customer_id = SalesOrder.objects.get(id=current_so_id).customer_name
    print_date = SalesOrder.objects.get(id=current_so_id).date
    discount = SalesOrder.objects.get(id=current_so_id).discount
    net_amt = SalesOrder.objects.get(id=current_so_id).net_amount
    total_amt = 0
    _id = SalesOrder.objects.get(id=pk).id
    for each in SoldItems.objects.filter(so_number__id=_id):
        total_amt += each.total_amt
    template_path = 'pdf/sales_order_pdf.html'
    context = {
        'current_so_id' : current_so_id,
        'print_date' : print_date,
        'sales_order_views' : sales_order_views,
        'discount' : discount,
        'net_amt'  : net_amt,
        'total_amt' : total_amt,
        'current_so_no' : current_so_no,
        'current_customer_id' : current_customer_id
        
        
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="sales_report.pdf"'
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


@login_required
def sales_payment(request):
    customers = Customer.objects.all()
    if request.method == "POST":  
        form = SelectCustomerForm(request.POST)
        c = request.POST.get('customer_id')
        c_id = Customer.objects.get(id=c).customer_id
        print("gwgw" ,c_id)
        return redirect('payment_customer', c_id)
        

    else:
        form = SelectCustomerForm()
    # if request.method == 'POST':
    #     v = request.POST.get('v_id')
    context = {
        "customers" : customers,
        "form" : form
    }
    return render(request, 'payment_sales/payment_add.html',context)  

@login_required
def payment_customer(request, customer_id):
    cid = Customer.objects.get(customer_id=customer_id).id
    current_customer_id = Customer.objects.get(id=cid).customer_id
    current_customer_name = Customer.objects.get(id=cid).customer_name
    sales_orders = SalesOrder.objects.filter(customer_name = cid).exclude(gross_amount=None)
    # po_id = PurchaseOrder.objects.get()
    
    context = {
        "current_customer_id" : current_customer_id,
        "current_customer_name" : current_customer_name,
        "sales_orders" : sales_orders,
    }
    return render(request, 'payment_sales/payment_customer.html',context)     

@login_required
def payment_sales_order(request,customer_id, pk):
    sales_orders = SalesOrder.objects.get(id=pk)
    sales_orders1 = SalesOrder.objects.all()
    current_so = SalesOrder.objects.get(id=pk).so_number
    current_cu = SalesOrder.objects.get(id=pk).customer_name
    current_id = SalesOrder.objects.get(id=pk).id
    net_total = SalesOrder.objects.get(id=pk).net_amount
    pending_amt = SalesOrder.objects.get(so_number=current_so).net_pending
    status = SalesOrder.objects.get(so_number=current_so).status
    
    payment_no = 101 if PaymentSales.objects.count() == 0 else PaymentSales.objects.aggregate(max=Max('payment_no'))["max"] + 1
    
    pending = SalesOrder.objects.get(id=pk).net_amount
    if request.method == "POST":
        paid_amt = request.POST.get('paid')
        
        if int(paid_amt) <= int(pending_amt):
            PaymentSales(payment_no=payment_no,payment_id=(f'{"TNR"}{payment_no}'),so_number=sales_orders1.get(so_number=current_so),paid=paid_amt).save()
            for each in PaymentSales.objects.filter(so_number__id=pk):
                    pending -= each.paid
            record = SalesOrder.objects.get(so_number=current_so)
            record.net_pending = pending
            record.save()
        else:
            return redirect('error_payment')
        return redirect('payment_sales_order',current_cu,current_id)
    sales_payments = PaymentSales.objects.filter(so_number_id=current_id)
    if pending_amt == 0:
        stat = SalesOrder.objects.get(so_number=current_so)
        stat.status = True
        stat.save()
        
    context = {
        "sales_orders" : sales_orders,
        "current_so" : current_so,
        "net_total" : net_total,
        # "pending" : pending,
        "sales_payments" : sales_payments
    }
    return render(request, 'payment_sales/payment_sales_order.html',context)   

def sales_return(request):
    if request.method == "POST":
        form = SelectSOForm(request.POST)
        so = request.POST.get('SalesOrderID')
        current_so = SalesOrder.objects.get(id=so)
        print("gwgw" ,so)
        return redirect('sales_return_po',current_so)
    else:
        form = SelectSOForm()
    context = {
        'form' : form,
    }
        
    return render(request, 'salesReturn/sales_return.html',context)    


def sales_return_po(request,so_number):
    items = Item.objects.all()
    current_so = so_number
    sn_id = SalesOrder.objects.get(so_number=so_number).id 
    sold_items = SoldItems.objects.filter(so_number_id = sn_id)
    if request.method == "POST":
        item_name = request.POST.get('i_name')
        re_qty = request.POST.get('rq')
        inm = Item.objects.get(name=item_name).id
        unit_price = Item.objects.get(id = inm).unit_price
        amt = int(re_qty) * int(unit_price)
        SalesReturn(so_number=SalesOrder.objects.get(so_number=current_so),item_name = items.get(name=item_name),return_qty = re_qty,amount=amt).save()
        record = Item.objects.get(id=inm)
        if int(re_qty) <= int(record.qty_sold):
            record.qty_sold = int(record.qty_sold) - int(re_qty)
            record.qty_purchased = int(record.qty_purchased) + int(re_qty)
            record.save()
            record2 = SalesOrder.objects.get(so_number=current_so)
            record2.net_amount = int(record2.net_amount) - int(amt)
            record2.net_pending = int(record2.net_pending) - int(amt)
            record2.save()
        else:
            return redirect('error_404')
        
        
        return redirect('sales_return_po', current_so)
        
    
    sales_returns = SalesReturn.objects.filter(so_number_id=sn_id)
    
        
    
    context = {
        'sold_items' : sold_items,
        'current_so' : current_so,
        'sales_returns' : sales_returns
    }
        
    return render(request, 'salesReturn/sales_return_po.html',context) 

@login_required
def error_404(request):
    return render(request, 'dashboard/error.html')

@login_required
def error_payment(request):
    return render(request, 'dashboard/error_payment.html')

@login_required
def re_order(request):
    items = Item.objects.filter(qty_purchased__lte=25)
    print(items)
    context = {
        'items' : items
    }
    return render(request, 'dashboard/re_order.html',context)

@login_required
def re_order_list(request):
    items = Item.objects.filter(qty_purchased__lte=25)
    print(items)
    template_path = 'pdf/re_order_pdf.html'
    context = {
        'items' : items
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="re_order_list.pdf"'
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








