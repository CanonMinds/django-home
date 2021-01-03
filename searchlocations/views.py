from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView

from .models import Location

class ProvincePageView(ListView):
    model = Location
    paginate_by = 20
    template_name = 'searchlocations/search_base.html'

    def get_queryset(self):
        return Location.objects.order_by('city')

class SearchResultsView(ListView):
    model = Location
    template_name = 'searchlocations/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Location.objects.filter(
            Q(city__icontains=query) | 
            Q(region__icontains=query) |
            Q(products__icontains=query) | 
            Q(area__icontains=query)
        )
        return object_list

def index(request):
    return HttpResponse('Done!') 