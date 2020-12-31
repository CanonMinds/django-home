from django.shortcuts import render

# Create your views here.
def greeting(request):
    return render(request, 'dynamicmapping/dm_index.html', )