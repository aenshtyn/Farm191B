from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Ledger
# from templates import *

# Create your views here.
def home(request):
    ledgers = Ledger.all_ledgers()

    return render(request, 'finance.html', {"ledgers" : ledgers})