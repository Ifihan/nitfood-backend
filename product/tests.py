from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

class TestFoodItemListCreateAPIView(APITestCase):
    def setUp(self):
        self.category = baker.make("product.Category")
        self.categorysize = baker.make("product.CategorySize", category=self.category)
        self.food = baker.make("product.Food", category=self.categorysize.category)
        self.food_item = baker.make("product.FoodItem", food=self.food)

    def test_get(self):
        url = reverse("product:food_items")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = reverse("product:food_items")
        payload = {
            "food": self.food.id,
            "market_name": "test market",
            "location": "test location",
            "size": self.food.category.sizes.first().id,
            "price": "1000",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_size(self):
        url = reverse("product:food_items")
        payload = {
            "food": self.food.id,
            "market_name": "test market",
            "location": "test location",
            "size": 100,
            "price": "1000",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "Invalid size")

    def test_post_invalid_food(self):
        url = reverse("product:food_items")
        payload = {
            "food": 100,
            "market_name": "test market",
            "location": "test location",
            "size": self.food.category.sizes.first().id,
            "price": "1000",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_post_invalid_food_size(self):
        url = reverse("product:food_items")
        payload = {
            "food": self.food.id,
            "market_name": "test market",
            "location": "test location",
            "size": 100,
            "price": "1000",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "Invalid size")
