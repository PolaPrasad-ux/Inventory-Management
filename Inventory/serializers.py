from rest_framework import serializers
from .models import InventoryItems

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryItems
        fields='__all__'