from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)

from . import models
from zeep import Client


def home(request):
    # print(-mzeep)
    # print(client)
    # context = {}
    template_name = 'soaptask/soaptask_index.html'
    return render(request, template_name)

def soapclient(request):
    val1 = int(request.GET['digit_1'])
    val2 = int(request.GET['digit_2'])
    given_numbers = [val1, val2]
    
    client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')

    total = client.service.Add(val1, val2)
    difference = client.service.Subtract(val1, val2)
    product = client.service.Multiply(val1, val2)
    quotient = client.service.Divide(val1, val2)

    context = { 'given_numbers': given_numbers,
        'total': total, 'difference': difference,
        'product': product,'quotient': quotient,}

    template_name = 'soaptask/soaptask_result.html'
    return render(request, template_name, context)

