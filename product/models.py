from django.db import models


class Category(models.Model):
    """Category Model."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class CategorySize(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="sizes", null=True
    )

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    food_image = models.ImageField(upload_to="static/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    """Model for the Food Items displayed on the home page by the admin."""

    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    market_name = models.CharField(max_length=250)
    location = models.CharField(max_length=500)
    size = models.ForeignKey(CategorySize, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.food.name} - {self.market_name} - {self.price}"
