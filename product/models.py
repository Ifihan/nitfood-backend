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


class Location(models.Model):
    """Model for the location to be chosen by the user"""

    name = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class MarketName(models.Model):
    """Model for the marketplace based on the location chosen by the user"""

    name = models.CharField(max_length=500, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Market-name: {self.name}"


class FoodItem(models.Model):
    """Model for the Food Items displayed on the home page by the admin."""

    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(
        Location, max_length=500, on_delete=models.SET_NULL, null=True
    )
    market_name = models.ForeignKey(
        MarketName, max_length=500, on_delete=models.SET_NULL, null=True
    )
    size = models.ForeignKey(CategorySize, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food.name} - {self.market_name} - {self.price}"

    @property
    def category(self):
        """Returns the category of the food."""
        return self.food.category if self.food else None

    @property
    def category_sizes(self):
        """Returns the sizes available for the food's category."""
        if self.food and self.food.category:
            return self.food.category.sizes.all()
        return CategorySize.objects.none()
