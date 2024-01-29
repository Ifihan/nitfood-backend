from django.contrib import admin

from product.models import Category, CategorySize, Food, FoodItem, Location, MarketName

admin.site.register(Food)
admin.site.register(FoodItem)
admin.site.register(Category)
admin.site.register(CategorySize)
admin.site.register(Location)
admin.site.register(MarketName)
