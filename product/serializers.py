from rest_framework import serializers

from .models import Category, Food, FoodItem, Location, MarketName, CategorySize


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class FoodSerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ["name", "food_image", "category", "sizes"]

    def get_sizes(self, food):
        return [
            {"id": size.id, "name": size.name} for size in food.category.sizes.all()
        ]


class ListFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["name", "food_image", "category"]


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["name"]


class ListFoodItemSerializer(serializers.ModelSerializer):
    food = FoodItemSerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields = ["id", "food", "location", "market_name", "size", "price"]


class EditCreateFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["id", "food", "market_name", "location", "size", "price"]


# ListFood sErializer
# override the create method. if the id is in the list,


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name", "created_at"]


class MarketPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketName
        fields = ["id", "name", "location", "created_at"]


class CategorySizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySize
        fields = ["id", "name", "category"]
