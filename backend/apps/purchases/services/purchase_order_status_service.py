from django.db import transaction
from django.db import models
from django.db import transaction

class PurchaseOrderStatusService:
    """
    Handles automatic Purchase Order status updates
    based on received quantities.
    """

    @staticmethod
    @transaction.atomic
    def update_status(purchase_order):
        """
        Update Purchase Order status based on
        Purchase Order Item received quantities.
        """

        items = purchase_order.items.all()

        if not items.exists():
            purchase_order.status = "DRAFT"
            purchase_order.save(
                update_fields=["status"]
            )
            return purchase_order

        total_quantity = 0
        received_quantity = 0

        for item in items:
            total_quantity += item.quantity
            received_quantity += item.received_quantity

        if received_quantity == 0:

            # PO approved but nothing received
            if purchase_order.status == "APPROVED":
                purchase_order.status = "ORDERED"

        elif received_quantity < total_quantity:

            purchase_order.status = "PARTIALLY_RECEIVED"

        else:

            purchase_order.status = "COMPLETED"

        purchase_order.save(
            update_fields=["status"]
        )

        return purchase_order

    @staticmethod
    def is_completed(purchase_order):
        """
        Returns True if every item
        has been fully received.
        """

        return all(
            item.remaining_quantity == 0
            for item in purchase_order.items.all()
        )

    @staticmethod
    def remaining_items(purchase_order):
        """
        Returns all items
        still pending receipt.
        """

        return purchase_order.items.filter(
            received_quantity__lt=models.F("quantity")
        )

    @staticmethod
    def completion_percentage(purchase_order):
        """
        Returns Purchase Order completion
        percentage.
        """

        items = purchase_order.items.all()

        total = sum(item.quantity for item in items)

        if total == 0:
            return 0

        received = sum(
            item.received_quantity
            for item in items
        )

        return round(
            (received / total) * 100,
            2,
        )