from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import Product

from .quotation import Quotation


class QuotationItem(BaseModel):
    """
    Sales Quotation Item
    """

    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="quotation_items",
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
            f"{self.quotation.quotation_number}"
            f" - {self.product.name}"
        )