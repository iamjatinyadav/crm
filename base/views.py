from django.shortcuts import render, redirect
from django.http import HttpResponse

from base.models import Customer, Order, Product
from .forms import Orderform
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


def createOrder(request):
    form = Orderform()
    if request.method == 'POST':
        # print('Printing Post:'request.POST)
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={"form":form}
    return render(request, "base/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form=Orderform( instance=order)
    if request.method == 'POST':
        # print('Printing Post:'request.POST)
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/') #means back to home 

    context={"form":form}
    return render(request, "base/order_form.html", context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context={'item':order}
    return render(request, "base/delete.html", context)
