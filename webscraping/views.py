from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)

import time
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from django.http import HttpResponse    

from . import models
 
def get_html_content(city):
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
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}')
    return html_content

def home(request):
    #First Scraping
    # source = requests.get('http://coreyms.com').text
    # soup = BeautifulSoup(source, 'lxml')
    # web_data = None
    # for article in soup.find_all('article'):
    #     web_data = {}
    #     web_data['headline'] = article.h2.a.text
    #     web_data['summary'] = article.find('div', class_='entry-content').p.text
    #     try:
    #         vid_src = article.find('iframe', class_='youtube-player')['src']
    #         vid_id = vid_src.split('/')[4]
    #         vid_id = vid_id.split('?')[0]
    #         web_data['yt_link'] = f'https://youtube.com/watch?v={vid_id}'
    #     except Exception as e:
    #         web_data['yt_link'] = None
    
    #Second Scraping with Issues
    # Has <Response 429> Issues
    # weather_data = None
    # if 'city' in request.GET:
        #Fetching the data
        # city = request.GET.get('city')
        # html_content = get_html_content(city)
        # soup = BeautifulSoup(html_content, 'html.parser')

        # weather_data = dict()
        # weather_data['region'] = soup.find('div', attrs={'id': 'wob_loc'}).text
        # weather_data['daytime'] = soup.find('div', attrs={'id': 'wob_dts'}).text
        # weather_data['status'] = soup.find('div', attrs={'id': 'wob_dc'}).text
        # weather_data['temp'] = soup.find('div', attrs={'id': 'wob_tm'}).text
        # print(html_content)
        
        # print(weather_data)
        # pass

    return render(request, 'webscraping/webscraping_list.html',)

def module1(request):
    #Third Scraping
    url1 = "https://timesofindia.indiatimes.com/briefs"
    toi_r = requests.get(url1)
    toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
    toi_headings = toi_soup.find_all('h2')
    toi_headings = toi_headings[0:-13]
    
    toi_news = []

    for th in toi_headings:
        toi_news.append(th.text)

    ht_r = requests.get("https://www.hindustantimes.com/india-news/")
    ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
    ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
    ht_headings = ht_headings[2:]
    ht_news = []

    for hth in ht_headings:
        ht_news.append(hth.text)

    return render(request, 'webscraping/webscraping_module1.html', 
    {'toi_news': toi_news, 'ht_news': ht_news , 'url1': url1, })

def module2(request):
    #Fourth Scraping
    url1 = "https://us.cnn.com/us"
    cnn_r = requests.get(url1)
    cnn_soup = BeautifulSoup(cnn_r.content, 'html5lib')
    cnn_headings = cnn_soup.find_all("span", class_="cd__headline-text")
    cnn_headings = cnn_headings[0:] # removing footers
    cnn_headlines = []

    for th in cnn_headings:
        cnn_headlines.append(th.text)

    return render(request, 'webscraping/webscraping_module2.html', 
    {'cnn_headlines': cnn_headlines, 'url1': url1, })

def module3(request):
    #Fourth Scraping
    url1 = "https://www.philstar.com/headlines"
    pr_r = requests.get(url1)
    pr_soup = BeautifulSoup(pr_r.content, 'html5lib')
    pr_headings = pr_soup.find_all("div", class_="news_title")
    pr_headingsTop = pr_soup.find_all("div", class_="topNews_title")
    pr_headingsSlider = pr_soup.find_all("div", class_="slider_title")

    pr_headings = pr_headings[0:]
    pr_headingsTop = pr_headingsTop[0:]
    pr_headingsSlider = pr_headingsSlider[0:]

    pr_headlines = []

    for th in pr_headingsSlider:
        pr_headlines.append(th.text)

    for th in pr_headingsTop:
        pr_headlines.append(th.text)

    for th in pr_headings:
        pr_headlines.append(th.text)

    print(pr_headlines)
    return render(request, 'webscraping/webscraping_module3.html', 
    {'pr_headlines': pr_headlines, 'url1': url1, })