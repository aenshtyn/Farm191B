from rest_framework import serializers
from finance.models import Ledger, Transaction
from hr.models import Employee, Owner
from inventory.models import Calf, Cow

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'

class CowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cow
        fields = '__all__'

class CalfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calf
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'