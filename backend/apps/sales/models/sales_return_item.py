from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import (
    Product,
    WarehouseLocation,
)

from .sales_return import SalesReturn
from .sales_invoice_item import SalesInvoiceItem


class SalesReturnItem(BaseModel):
    """
    Sales Return Item
    """

    sales_return = models.ForeignKey(
        SalesReturn,
        on_delete=models.CASCADE,
        related_name="items",
    )

    sales_invoice_item = models.ForeignKey(
        SalesInvoiceItem,
        on_delete=models.PROTECT,
        related_name="return_items",
        null=True,
        blank=True,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="sales_return_items",
    )

    location = models.ForeignKey(
        WarehouseLocation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_return_items",
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    refund_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    condition = models.CharField(
        max_length=20,
        choices=[
            ("GOOD", "Good"),
            ("DAMAGED", "Damaged"),
            ("DEFECTIVE", "Defective"),
            ("SCRAP", "Scrap"),
        ],
        default="GOOD",
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
            f"{self.sales_return.return_number}"
            f" - {self.product.name}"
        )