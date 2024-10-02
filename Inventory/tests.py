from rest_framework.test import APITestCase

#Create your tests here.

from django.urls import reverse

from rest_framework.test import APITestCase



from rest_framework import status

from .models import InventoryItems

# Create your tests here.

class ItemAPITestCase (APITestCase):
    def setUp(self):

        self.item = InventoryItems.objects.create(name='Test Item', category="top", description="Test",price=100, quantity=10) 

    def test_get_item_list(self): 
        url = reverse('item-list')

        response=self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_item(self):

        url=reverse('item-list')

        data = [{'name': 'New Item', 'category': 'top','description':"Test", 'price': 208, 'quantity': 5}]

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_delete_item(self):

        url = reverse('item-detail', kwargs={'pk': self.item.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

