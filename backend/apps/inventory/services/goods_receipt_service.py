from django.db import transaction

from apps.inventory.models import StockTransaction
from apps.inventory.services.stock_service import StockService

from apps.inventory.services.stock_transaction_service import (
    StockTransactionService,
)

class GoodsReceiptService:
    """
    Handles receiving inventory from suppliers.
    """

    @staticmethod
    @transaction.atomic
    def receive_item(
        goods_receipt,
        goods_receipt_item,
    ):
        po_item = goods_receipt_item.purchase_order_item

        # Prevent over receiving
        remaining = (
            po_item.quantity -
            po_item.received_quantity
        )

        if goods_receipt_item.accepted_quantity > remaining:
            raise ValueError(
                "Received quantity exceeds remaining quantity."
            )

        # Update Purchase Order Item
        po_item.received_quantity += (
            goods_receipt_item.accepted_quantity
        )

        po_item.save()

        # Increase Stock
        StockService.increase_stock(
            product=goods_receipt_item.product,
            warehouse=goods_receipt.warehouse,
            location = goods_receipt_item.location,
            quantity=goods_receipt_item.accepted_quantity,
        )

        # Create Stock Transaction
        StockTransactionService.create_transaction(
    product=goods_receipt_item.product,
    warehouse=goods_receipt.warehouse,
    location=goods_receipt_item.location,
    transaction_type="PURCHASE",
    quantity=goods_receipt_item.accepted_quantity,
    reference_number=goods_receipt.receipt_number,
    remarks="Goods Receipt",
    created_by=goods_receipt.received_by,
)

        return True