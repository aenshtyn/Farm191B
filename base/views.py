from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from inventory.models import Cow, MorningMilk
from hr.models import Owner

# Create your views here.

# def dashboard_view(request):
    
# 	return render(request, 'dashboard.html', {})

def pie_chart(request):
    labels = []
    data = []

    queryset = Cow.objects.order_by('-age')
    for cow in queryset:
        labels.append(cow.name)
        data.append(cow.age)

    return render(request, 'index.html', {
        'labels': labels,
        'data': data,
    })

def morning_milk_production(request):
    labels = []
    data = []

    queryset = MorningMilk.objects.order_by('-volume')
    for morningmilk in queryset:
        labels.append(morningmilk.date)
        data.append(morningmilk.volume)

    return render(request, 'morning_milk.html', {
        'labels': labels,
        'data': data,
    })
        

def index(request):
    return render(request,'index.html')
