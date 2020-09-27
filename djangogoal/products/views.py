from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse
import json

# Create your views here.

from .models import *

# class ProductsView(View):
#     def get(self, request):
#         return HttpResponse("Welcome to our Shopping Cart!")

# class ProductsView(TemplateView):
#     template_name = "products.html"
 
def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() #Parent-Child querying'
        cartItems = order.get_cart_items

    else:
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        items = []
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'products/store.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() #Parent-Child querying
        cartItems = order.get_cart_items

    else:
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        items = []
        cartItems = order['get_cart_items']
        
    context = {'items':items,'order':order, 'cartItems': cartItems, }
    return render(request, 'products/cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() #Parent-Child querying
        cartItems = order.get_cart_items

    else:
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        items = []
        cartItems = order['get_cart_items']

    context = {'items':items,'order':order, 'cartItems': cartItems}
    return render(request, 'products/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)