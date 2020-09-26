from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

# class ProductsView(View):
#     def get(self, request):
#         return HttpResponse("Welcome to our Shopping Cart!")

# class ProductsView(TemplateView):
#     template_name = "products.html"

def store(request):
    context = {}
    return render(request, 'products/store.html', context)

def cart(request):
    context = {}
    return render(request, 'products/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'products/checkout.html', context)