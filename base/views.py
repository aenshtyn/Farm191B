from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404

# Create your views here.

def dashboard_view(request):
    
	return render(request, 'dashboard.html', {})