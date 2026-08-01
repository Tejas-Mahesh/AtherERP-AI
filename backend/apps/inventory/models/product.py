from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization

from .category import Category
from .brand import Brand
from .unit import Unit


class Product(BaseModel):
    """
    Product Master
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="products",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        related_name="products",
    )

    name = models.CharField(
        max_length=200,
    )

    sku = models.CharField(
        max_length=50,
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
    )

    cost_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    reorder_level = models.PositiveIntegerField(
        default=10,
    )

    minimum_stock = models.PositiveIntegerField(
        default=0,
    )

    maximum_stock = models.PositiveIntegerField(
        default=1000,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:

        ordering = [
            "name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "sku",
                ],
                name="unique_product_sku_per_organization",
            ),
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "barcode",
                ],
                name="unique_product_barcode_per_organization",
            ),
        ]

    def __str__(self):
        return f"{self.sku} - {self.name}"