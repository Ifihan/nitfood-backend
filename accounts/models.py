from django.db import models


class CustomUser(models.Model):
    """Custom user model."""

    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(blank=False, max_length=255)
    password = models.CharField(max_length=255, blank=False)
    password2 = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name
