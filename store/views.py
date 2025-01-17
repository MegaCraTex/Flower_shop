from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CustomerForm, ProductForm, PurchaseForm
from .models import Customer, Product, Purchase

def home(request):
    return render(request, 'store/home.html')

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'store/add_customer.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'store/edit_customer.html', {'form': form})

def customer_list(request):
    query = request.GET.get('q')
    if query:
        customers = Customer.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        customers = Customer.objects.all()

    paginator = Paginator(customers, 10)  # Show 10 customers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/customer_list.html', {'page_obj': page_obj, 'query': query})

# Repeat similar changes for products and purchases
# ...

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'form': form})

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(stock_quantity__icontains=query)
        )
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/product_list.html', {'page_obj': page_obj, 'query': query})

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'store/add_purchase.html', {'form': form})

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'store/purchase_list.html', {'purchases': purchases})