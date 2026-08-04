from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import Product

from .sales_order import SalesOrder


class SalesOrderItem(BaseModel):
    """
    Sales Order Item
    """

    sales_order = models.ForeignKey(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="sales_order_items",
    )

    description = models.TextField(
        blank=True,
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

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

    delivered_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    invoiced_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    class Meta:

        ordering = [
            "id",
        ]

    @property
    def remaining_delivery_quantity(self):
        return self.quantity - self.delivered_quantity

    @property
    def remaining_invoice_quantity(self):
        return self.quantity - self.invoiced_quantity

    def __str__(self):
        return (
            f"{self.sales_order.sales_order_number}"
            f" - {self.product.name}"
        )