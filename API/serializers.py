from rest_framework import serializers
from finance.models import Ledger, Transaction
from hr.models import Employee
from inventory.models import Calf, Cow

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'