from rest_framework import serializers

from .models import Category, Food, FoodItem


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


class ListFoodItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer()

    class Meta:
        model = FoodItem
        fields = ["id", "food", "market_name", "location", "size", "price"]


class EditCreateFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["id", "food", "market_name", "location", "size", "price"]


# ListFood sErializer
# override the create method. if the id is in the list,
