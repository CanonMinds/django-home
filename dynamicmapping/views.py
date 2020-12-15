from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)
 
def home(request):
    template_name = 'dynamicmapping/dm_index.html'
    return render(request, template_name,  )

def interior(request):
    template_name = 'dynamicmapping/dm_layer.html'
    return render(request, template_name,  )

def polygon(request):
    template_name = 'dynamicmapping/dm_polygon.html'
    return render(request, template_name,  )