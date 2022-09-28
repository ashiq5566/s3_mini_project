from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer, Vendor, Item
from django.contrib.auth.models import User
from .forms import CustomerForm, VendorForm, ItemForm
from django.contrib import messages
from django.db.models import Q

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
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
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
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
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
    if request.method == 'POST':
        # i_id = request.POST.get('item_id')
        # name = request.POST.get('item_name')
        # Item(item_id=i_id,name=name).save()
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/stock.html',context)
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




