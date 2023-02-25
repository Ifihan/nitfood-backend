from django.contrib import admin

from product.models import Category, CategorySize, Food, FoodItem

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(CategorySize)
admin.site.register(FoodItem)
