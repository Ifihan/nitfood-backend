from django.urls import path
from product.views import FoodItemListCreateAPIView

app_name = "product"

urlpatterns = [
    path("", FoodItemListCreateAPIView.as_view(), name="food-items"),
]