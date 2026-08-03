from django.db import models

from apps.common.models import BaseModel
from apps.accounts.models import User

from .product import Product
from .warehouse import Warehouse
from .warehouse_location import WarehouseLocation


class StockTransaction(BaseModel):
    """
    Inventory Ledger
    """

    TRANSACTION_TYPES = [
        ("PURCHASE", "Purchase"),
        ("SALE", "Sale"),
        ("TRANSFER_IN", "Transfer In"),
        ("TRANSFER_OUT", "Transfer Out"),
        ("ADJUSTMENT", "Adjustment"),
        ("RETURN_IN", "Return In"),
        ("RETURN_OUT", "Return Out"),
        ("OPENING", "Opening Stock"),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="stock_transactions",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="stock_transactions",
    )

    location = models.ForeignKey(
        WarehouseLocation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stock_transactions",
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES,
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    reference_number = models.CharField(
        max_length=50,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stock_transactions",
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return (
            f"{self.product.name} "
            f"- {self.transaction_type} "
            f"({self.quantity})"
        )