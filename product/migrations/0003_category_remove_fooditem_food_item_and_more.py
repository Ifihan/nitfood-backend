# Generated by Django 4.1.7 on 2023-02-23 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_fooditem_food_item"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="fooditem",
            name="food_item",
        ),
        migrations.RemoveField(
            model_name="fooditem",
            name="size",
        ),
        migrations.AddField(
            model_name="fooditem",
            name="food_image",
            field=models.ImageField(default=[], upload_to="static/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fooditem",
            name="name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fooditem",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name="CategorySize",
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
                ("name", models.CharField(max_length=50)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sizes",
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="fooditem",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product.category",
            ),
        ),
        migrations.DeleteModel(
            name="FoodImage",
        ),
    ]
