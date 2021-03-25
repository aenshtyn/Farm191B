from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Employee

# Create your views here.
def hr(request):
    employees = Employee.all_employees()

    return render(request, 'hr.html', {"employees": employees})

