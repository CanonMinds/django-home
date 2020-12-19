from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import Province

class ProvincePageView(ListView):
    model = Province
    template_name = 'searchlocations/search_base.html'

class SearchResultsView(ListView):
    model = Province
    template_name = 'searchlocations/search_results.html'
    # queryset = model.objects.filter(name__icontains='Laguna')

    def get_queryset(self):
        # return Province.objects.filter(name__icontains='Laguna')
                # object_list = Province.objects.filter(
        #     Q(name__icontains=query) | Q(region__icontains=query)
        # )

        query = self.request.GET.get('q')
        object_list = Province.objects.filter(
            Q(city__icontains=query) | 
            Q(region__icontains=query) |
            Q(products__icontains=query) | 
            Q(area__icontains=query)
        )
        return object_list

def index(request):
    return HttpResponse('Done!') 