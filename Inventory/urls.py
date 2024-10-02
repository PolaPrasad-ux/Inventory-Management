from .views import *
from django.urls import path

urlpatterns = [
    path('inventory/items/', ItemListCreateAPIView.as_view(),name='item-list'),

    path('inventory/items/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(),name='item-detail'),

    path('items/query/<str:category>/', ItemCategoryAPIView.as_view()),

    path('items/sort/',ItemSortByPriceAPIView.as_view())
   
] 