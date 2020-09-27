from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

from .models import *

# class ProductsView(View):
#     def get(self, request):
#         return HttpResponse("Welcome to our Shopping Cart!")

# class ProductsView(TemplateView):
#     template_name = "products.html"
 
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/store.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() #Parent-Child querying
    else:
        order = {'get_cart_total':0, 'get_cart_items':0, }
        items = []
        
    context = {'items':items,'order':order}
    return render(request, 'products/cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() #Parent-Child querying
    else:
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []

    context = {'items':items,'order':order}
    return render(request, 'products/checkout.html', context)