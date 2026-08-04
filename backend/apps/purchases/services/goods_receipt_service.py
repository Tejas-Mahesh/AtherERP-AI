from django.db import transaction

from apps.inventory.services.stock_service import StockService
from apps.inventory.services.stock_transaction_service import (
    StockTransactionService,
)

from apps.purchases.services.purchase_order_status_service import (
    PurchaseOrderStatusService,
)


class GoodsReceiptService:
    """
    Handles Goods Receipt processing.

    Responsibilities:
        - Validate received quantity
        - Update Purchase Order Item
        - Increase Stock
        - Create Stock Transaction
        - Update Purchase Order Status
    """

    @staticmethod
    @transaction.atomic
    def receive_item(
        goods_receipt,
        goods_receipt_item,
    ):
        """
        Process a single Goods Receipt Item.
        """

        po_item = goods_receipt_item.purchase_order_item

        remaining_quantity = (
            po_item.quantity -
            po_item.received_quantity
        )

        if goods_receipt_item.accepted_quantity > remaining_quantity:
            raise ValueError(
                "Received quantity exceeds remaining quantity."
            )

        # -----------------------------------------
        # Update Purchase Order Item
        # -----------------------------------------

        po_item.received_quantity += (
            goods_receipt_item.accepted_quantity
        )

        po_item.save(
            update_fields=[
                "received_quantity",
            ]
        )

        # -----------------------------------------
        # Increase Warehouse Stock
        # -----------------------------------------

        StockService.increase_stock(
            product=goods_receipt_item.product,
            warehouse=goods_receipt.warehouse,
            quantity=goods_receipt_item.accepted_quantity,
        )

        # -----------------------------------------
        # Inventory Ledger Entry
        # -----------------------------------------

        StockTransactionService.purchase(
            product=goods_receipt_item.product,
            warehouse=goods_receipt.warehouse,
            location=goods_receipt_item.location,
            quantity=goods_receipt_item.accepted_quantity,
            reference_number=goods_receipt.receipt_number,
            created_by=goods_receipt.received_by,
        )

        # -----------------------------------------
        # Update Purchase Order Status
        # -----------------------------------------

        PurchaseOrderStatusService.update_status(
            po_item.purchase_order
        )

        return goods_receipt_item

    @staticmethod
    @transaction.atomic
    def receive_all(goods_receipt):
        """
        Receive every item in the Goods Receipt.
        """

        for item in goods_receipt.items.all():
            GoodsReceiptService.receive_item(
                goods_receipt,
                item,
            )

        return goods_receipt

    @staticmethod
    def validate(goods_receipt_item):
        """
        Validate Goods Receipt Item.
        """

        if goods_receipt_item.accepted_quantity < 0:
            raise ValueError(
                "Accepted quantity cannot be negative."
            )

        if goods_receipt_item.received_quantity < 0:
            raise ValueError(
                "Received quantity cannot be negative."
            )

        if (
            goods_receipt_item.accepted_quantity >
            goods_receipt_item.received_quantity
        ):
            raise ValueError(
                "Accepted quantity cannot exceed received quantity."
            )

        if goods_receipt_item.rejected_quantity < 0:
            raise ValueError(
                "Rejected quantity cannot be negative."
            )

        return True