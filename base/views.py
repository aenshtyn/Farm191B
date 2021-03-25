from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from inventory.models import Cow

# Create your views here.

# def dashboard_view(request):
    
# 	return render(request, 'dashboard.html', {})

def pie_chart(request):
    labels = []
    data = []

    queryset = Cow.objects.order_by('owner')[:5]
    for cow in queryset:
        labels.append(cow.name)
        data.append(cow.owner)

    return render(request, 'dashboard.html', {
        'labels': labels,
        'data': data,
    })