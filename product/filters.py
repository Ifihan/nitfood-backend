from django_filters import rest_framework as filters

from .models import Category, CategorySize, Food, Location, MarketName, FoodItem


# class CategoryFilter(filters.FilterSet):
#     class Meta:
#         model = Category
#         fields = ["name"]


class CategorySizeFilter(filters.FilterSet):
    category = filters.CharFilter(method="filter_category")

    class Meta:
        model = CategorySize
        fields = ["category"]

    def filter_category(self, queryset, name, value):
        return queryset.filter(category__pk=value)


class MarketNameFilter(filters.FilterSet):
    location = filters.CharFilter(method="filter_location")

    class Meta:
        model = MarketName
        fields = ["location"]

    def filter_location(self, queryset, name, value):
        return queryset.filter(location__pk=value)


# class FoodItemFilter(filters.FilterSet):
