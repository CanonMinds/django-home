from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from django.http import HttpResponse    
import time
from time import sleep

from . import models

class WebListView(ListView):
    context_object_name = "webdata"
    # fields = ("municipality", "region")
    # model = LocalShelterPlan, Region
    template_name = "webscraping/webscraping_list.html"

    # url = form.cleaned_data.get['http://www.unece.org/cefact/locode/service/location']
    # data = requests.get(url)
    def __init__(self):
        print("Starting Now")
        self.get_html_content    

    def get_html_content(self, city):
        USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)    
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        city = city.replace('','+')
        html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
        # response = HttpResponse(html_content)
        # print(response)
        # if response.status_code == 429:
        #     time.sleep(int(response.headers["Retry-After"]))
        # URL = 'https://www.google.com/search?q=weather+in+{city}'
        # html_content = requests.get(URL)
        # print(html_content)
        return html_content

    def get(self, request):
        if 'city' in request.GET:
            #Fetching the data
            city = request.GET.get('city')
            html_content = self.get_html_content(city)
            print(html_content)
            pass
        # lsp_plans_list = LocalShelterPlan.objects.all()
        # region = Region.objects.order_by('name')
        # lsp_plans_count = LocalShelterPlan.objects.all().count()
        # context_data = {'lsp_plans_count': lsp_plans_count, 'lsp_plans_list': lsp_plans_list, 'region': region}
        return render(request, self.template_name)