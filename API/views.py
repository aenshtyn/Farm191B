from django.shortcuts import render
from rest_framework import viewsets
from API.serializers import LedgerSerializer
from finance.models import Ledger

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer