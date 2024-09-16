from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # return HttpResponse("this is home page")
    # return render(request,"index.html")  #ei index alaway globally open kroa folder er vitorer file dhorbe
    return render(request,'first_app/home.html')   # by default django is configured to know where to look for templates.. in settings.py 
