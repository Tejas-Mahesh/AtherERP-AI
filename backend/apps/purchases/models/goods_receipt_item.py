from django.db import models

from apps.common.models import BaseModel
from apps.inventory.models import Product
from apps.inventory.models import WarehouseLocation
from .goods_receipt import GoodsReceipt
from .purchase_item import PurchaseOrderItem


class GoodsReceiptItem(BaseModel):
    """
    Goods Receipt Item
    """

    goods_receipt = models.ForeignKey(
        GoodsReceipt,
        on_delete=models.CASCADE,
        related_name="items",
    )

    purchase_order_item = models.ForeignKey(
        PurchaseOrderItem,
        on_delete=models.PROTECT,
        related_name="goods_receipt_items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="goods_receipt_items",
    )
    location = models.ForeignKey(
    WarehouseLocation,
    on_delete=models.PROTECT,
    related_name="goods_receipt_items",
    null=True,
    blank=True,
)
    ordered_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    received_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    accepted_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    rejected_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return (
            f"{self.goods_receipt.receipt_number} "
            f"- {self.product.name}"
        )