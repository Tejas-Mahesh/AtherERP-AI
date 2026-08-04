from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import (
    Product,
    WarehouseLocation,
)

from .delivery_note import DeliveryNote
from .sales_order_item import SalesOrderItem


class DeliveryNoteItem(BaseModel):
    """
    Delivery Note Item
    """

    delivery_note = models.ForeignKey(
        DeliveryNote,
        on_delete=models.CASCADE,
        related_name="items",
    )

    sales_order_item = models.ForeignKey(
        SalesOrderItem,
        on_delete=models.PROTECT,
        related_name="delivery_items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="delivery_items",
    )

    location = models.ForeignKey(
        WarehouseLocation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="delivery_items",
    )

    ordered_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    delivered_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = [
            "id",
        ]

    def __str__(self):
        return (
            f"{self.delivery_note.delivery_number}"
            f" - {self.product.name}"
        )