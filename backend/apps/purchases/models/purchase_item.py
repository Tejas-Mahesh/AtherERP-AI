from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import Product

from .purchase_order import PurchaseOrder


class PurchaseOrderItem(BaseModel):
    """
    Purchase Order Item
    """

    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="purchase_items",
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    discount_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    tax_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    line_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    received_quantity = models.PositiveIntegerField(
        default=0,
    )

    class Meta:

        ordering = [
            "id",
        ]

    @property
    def remaining_quantity(self):
        return self.quantity - self.received_quantity

    def __str__(self):
        return (
            f"{self.purchase_order.purchase_number}"
            f" - {self.product.name}"
        )