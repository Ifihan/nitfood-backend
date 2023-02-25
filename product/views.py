from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status

from product.models import Food, FoodItem
from product.serializers import EditCreateFoodItemSerializer, ListFoodItemSerializer


class FoodItemListCreateAPIView(generics.ListCreateAPIView):
    """View for uploading or retrieving food items."""

    # uncomment permission class later after setting up email verification
    queryset = FoodItem.objects.all()

    # permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListFoodItemSerializer
        return EditCreateFoodItemSerializer

    def post(self, request, **kwargs):
        size_id = int(request.data.get("size"))
        food_id = request.data.get("food")
        food = get_object_or_404(Food.objects.all(), id=food_id)
        food_sizes = [item.id for item in food.category.sizes.all()]

        if size_id not in food_sizes:
            return response.Response(
                {"message": "Invalid size"}, status=status.HTTP_400_BAD_REQUEST
            )
        # super(self).post(request, **kwargs)
        return self.create(request, **kwargs)
