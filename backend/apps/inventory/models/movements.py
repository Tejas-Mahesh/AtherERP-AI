from django.db import models

from apps.common.models import BaseModel

from .product import Product
from .warehouse import Warehouse


class StockMovement(BaseModel):
    """
    Stock Movement History
    """

    MOVEMENT_TYPES = [
        ("IN", "Stock In"),
        ("OUT", "Stock Out"),
        ("TRANSFER", "Transfer"),
        ("ADJUSTMENT", "Adjustment"),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="movements",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="movements",
    )

    movement_type = models.CharField(
        max_length=20,
        choices=MOVEMENT_TYPES,
    )

    quantity = models.PositiveIntegerField()

    reference = models.CharField(
        max_length=100,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    def __str__(self):
        return (
            f"{self.product.name} - "
            f"{self.movement_type}"
        )