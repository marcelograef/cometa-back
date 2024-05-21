from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class StockAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_stock(self):
        response = self.client.get(reverse('stock'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('last_updated', response.data)
        self.assertIn('beers', response.data)

class OrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_order(self):
        response = self.client.get(reverse('order'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('created', response.data)
        self.assertIn('rounds', response.data)
