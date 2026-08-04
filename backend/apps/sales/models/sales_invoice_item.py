from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import Product

from .sales_invoice import SalesInvoice
from .sales_order_item import SalesOrderItem


class SalesInvoiceItem(BaseModel):
    """
    Sales Invoice Item
    """

    sales_invoice = models.ForeignKey(
        SalesInvoice,
        on_delete=models.CASCADE,
        related_name="items",
    )

    sales_order_item = models.ForeignKey(
        SalesOrderItem,
        on_delete=models.PROTECT,
        related_name="invoice_items",
        null=True,
        blank=True,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="sales_invoice_items",
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

    class Meta:

        ordering = [
            "id",
        ]

    def __str__(self):
        return (
            f"{self.sales_invoice.invoice_number}"
            f" - {self.product.name}"
        )