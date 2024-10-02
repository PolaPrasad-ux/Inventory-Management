from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import InventoryItems
from django.core.cache import cache
import logging
from Inventory.serializers import ItemSerializer
# Create your views here.
logger=logging.getLogger('Inventory')
class ItemListCreateAPIView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def post(self, request, *args, **kwargs):
        serializer=ItemSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            # logger.info(f"Item Created:{serializer.data[0]['name']}")
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        logger.error(f"Failed to create:{serializer.errors}")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):


        cached_data=cache.get('item_response110')
        if cached_data:
            logger.info(f"Cache hit at item successfully")
        if cached_data is None:
            print('redis working')

            items = InventoryItems.objects.all()

            serializer = ItemSerializer(items, many=True)
            cache.set('item_response110', serializer.data)
            
        return Response (cached_data, status=status.HTTP_200_OK)

class ItemRetrieveUpdateDestroyAPIView (APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def delete(self, request, pk, *args, **kwargs):

        try:

            item = InventoryItems.objects.get(pk=pk)

        except InventoryItems.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        item.delete()

        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):

        try:

            item = InventoryItems.objects.get(pk=pk)

        except InventoryItems.DoesNotExist:

            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ItemSerializer(item, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):

        try:

            item = InventoryItems.objects.get(pk=pk)

        except InventoryItems. DoesNotExist:

            return Response (status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(item)

        return Response (serializer.data, status=status.HTTP_200_OK)
            

    
class ItemCategoryAPIView(APIView):


    def get(self, request, category, *args, **kwargs): 
        items = InventoryItems.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True) 
        return Response (serializer.data, status=status.HTTP_200_OK)

class ItemSortByPriceAPIView(APIView):
     def get(self, request, *args, **kwargs):
        items = InventoryItems.objects.order_by('-price')
        serializer = ItemSerializer(items, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

