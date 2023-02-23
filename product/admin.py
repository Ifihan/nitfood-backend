from django.contrib import admin

from product.models import FoodItem, Category, CategorySize, Food

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(CategorySize)
admin.site.register(FoodItem)