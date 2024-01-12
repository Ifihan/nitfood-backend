# Generated by Django 4.1.7 on 2024-01-12 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_location_fooditem_is_published_marketplace"),
    ]

    operations = [
        migrations.CreateModel(
            name="MarketName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "location_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="product.location",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="MarketPlace",
        ),
    ]
