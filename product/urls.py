from django.urls import path

from product.views import (
    FoodItemListCreateAPIView,
    CategorySizeAPIView,
    MarketNameAPIView,
    FoodAPIView,
)

app_name = "product"

urlpatterns = [
    path("category-size/", CategorySizeAPIView.as_view(), name="category-size"),
    path("market-name/", MarketNameAPIView.as_view(), name="market-name"),
    path("food/", FoodAPIView.as_view(), name="food"),
    path("", FoodItemListCreateAPIView.as_view(), name="food_items"),
]
