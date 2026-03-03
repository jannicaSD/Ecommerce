from django.shortcuts import render

# Create your views here.
def eapp_list(request): 
    return render(request, 'eapp/eapp_list.html')