from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Calf, Cow

# Create your views here.
def inventory(request):
    cows = Cow.all_cows()
    
    return render(request,'inventory.html', {"cows": cows})
