from django.shortcuts import render
from django.http import HttpResponse

from base.models import Customer, Order, Product
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    panding = orders.filter(status='panding').count()
    context = {'orders': orders,
    'customers':customers, 'total_customer':total_customers, 'total_orders':total_orders, 'delivered': delivered, 'panding':panding}
    return render(request, 'base/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'base/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context= {'customer':customer, 'orders':orders, 'order_count': order_count}
    return render(request, 'base/customers.html', context)


def order_form(request):
    context={}
    return render(request, "base/order_form.html", context)
