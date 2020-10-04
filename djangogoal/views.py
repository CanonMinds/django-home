from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# def home(request):
#     return render(request,'home.html')

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games_today"] = 6
        return context

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World!")

        
def signupPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'signup.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)



#Remember
#DetailView expects URL argument of either slug or pk