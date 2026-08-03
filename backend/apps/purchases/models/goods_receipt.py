from django.db import models

from apps.common.models import BaseModel
from apps.accounts.models import User
from apps.inventory.models import Warehouse

from .purchase_order import PurchaseOrder


class GoodsReceipt(BaseModel):
    """
    Goods Receipt Note (GRN)
    """

    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name="goods_receipts",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="goods_receipts",
    )

    receipt_number = models.CharField(
        max_length=30,
        unique=True,
    )

    receipt_date = models.DateField()

    received_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="goods_receipts",
)

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = [
            "-receipt_date",
        ]

    def __str__(self):
        return self.receipt_number