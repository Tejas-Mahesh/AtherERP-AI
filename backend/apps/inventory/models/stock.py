from django.db import models

from apps.common.models import BaseModel

from .product import Product
from .warehouse import Warehouse


class Stock(BaseModel):
    """
    Product Stock in Warehouse
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="stocks",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="stocks",
    )

    quantity = models.PositiveIntegerField(
        default=0,
    )

    reserved_quantity = models.PositiveIntegerField(
        default=0,
    )

    last_stock_update = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "product__name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "product",
                    "warehouse",
                ],
                name="unique_product_stock_per_warehouse",
            ),
        ]

    @property
    def available_quantity(self):
        return self.quantity - self.reserved_quantity

    @property
    def inventory_value(self):
        return self.quantity * self.product.cost_price

    def __str__(self):
        return (
            f"{self.product.name} "
            f"({self.warehouse.name})"
        )