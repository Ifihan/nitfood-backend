from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestFoodItemListCreateAPIView(APITestCase):
    def test_food_item_list_create_api_view(self):
        url = reverse("food_items")
