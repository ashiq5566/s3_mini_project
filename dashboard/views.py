from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer, Vendor, Item,MyUUIDModel
from django.contrib.auth.models import User
from .forms import CustomerForm, VendorForm, ItemForm
from django.contrib import messages
from django.db.models import Q, Max

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
    c_id = 1 if Customer.objects.count() == 0 else Customer.objects.aggregate(max=Max('customer_no'))["max"] + 1
    if request.method == 'POST':
        cu_id = request.POST.get('cu_id')
        name = request.POST.get('c_name')
        address = request.POST.get('c_address')
        mob = request.POST.get('c_mob')
        Customer(customer_no=c_id,customer_id=(f'{"C00"}{c_id}'),customer_name=name,customer_address=address,customer_mobile=mob).save()
    # if request.method == 'POST':
        # form = CustomerForm(request.POST)
        # if form.is_valid():
        #     form.save()
            # redirect('dashboard/customer')
    # else:
    #     form = CustomerForm()
    context = {
        'customers': customers,
        'workers' : workers,
        'workers_count' : workers_count,
        'customer_count' : customer_count,
        'vendor_count' : vendor_count,
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
    v_id = 1 if Vendor.objects.count() == 0 else Vendor.objects.aggregate(max=Max('vendor_no'))["max"] + 1
    if request.method == 'POST':
        ve_id = request.POST.get('ve_id')
        name = request.POST.get('v_name')
        address = request.POST.get('v_address')
        mob = request.POST.get('v_mob')
        Vendor(vendor_no=v_id,vendor_id=(f'{"V00"}{v_id}'),vendor_name=name,vendor_address=address,vendor_mobile=mob).save()
    # if request.method == 'POST':
    #     form = VendorForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            # redirect('dashboard/vendor')


    # else:
    #     form = VendorForm()
    context = {
        # 'form' : form,  
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
    p_id = 1 if Item.objects.count() == 0 else Item.objects.aggregate(max=Max('item_no'))["max"] + 1
    if request.method == 'POST':
        i_id = request.POST.get('i_id')
        price = request.POST.get('uprice')
        name = request.POST.get('pname')
        Item(item_no=p_id,item_id=(f'{"P00"}{p_id}'),name=name,unit_price=price).save()
        # form = ItemForm(request.POST)
        # if form.is_valid():
        #     form.save()
    # else:
    #     form = ItemForm
    context = {
        'items': items,
        # 'form' : form,
    }
    return render(request, 'dashboard/stock.html',context)
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




