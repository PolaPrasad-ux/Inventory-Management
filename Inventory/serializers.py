from rest_framework import serializers
from .models import Inventory

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields='__all__'