from django.shortcuts import render
from django.http import HttpResponse

def flashword(request, username):
    template_name = 'greetings/index.html'
    context = {'username' : username,}
    return render(request, template_name, context )

def home(request):
    template_name = 'greetings/index.html'
    return render(request, template_name )