from rest_framework import serializers
from .models import Assets, Liabilities, Expenses
from django.contrib.auth.models import User

class AssetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('name', 'worth', 'type_of_object')

class LiabilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Liabilities
        fields = ('name', 'worth', 'type_of_object')

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('name', 'worth', 'type_of_object')

