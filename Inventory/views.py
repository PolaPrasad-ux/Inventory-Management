from django.shortcuts import render
from rest_framework import APIView,status,generics
from rest_framework.response import Response


from Inventory.serializers import ItemSerializer
# Create your views here.

class ItemListCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer=ItemSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

