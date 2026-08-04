from django.db import transaction

from apps.inventory.services.stock_service import (
    StockService,
)

from apps.inventory.services.stock_transaction_service import (
    StockTransactionService,
)

from apps.sales.models import SalesReturn


class SalesReturnService:
    """
    Business logic for Sales Returns.
    """

    @staticmethod
    @transaction.atomic
    def calculate_total(sales_return):
        """
        Calculate total refund amount.
        """

        total = 0

        for item in sales_return.items.all():

            item.refund_amount = (
                item.quantity * item.unit_price
            )

            item.save()

            total += item.refund_amount

        sales_return.total_amount = total
        sales_return.save()

        return sales_return

    @staticmethod
    @transaction.atomic
    def receive_return(
        sales_return,
        received_by=None,
    ):
        """
        Receive returned items.
        """

        if sales_return.status != "DRAFT":
            raise ValueError(
                "Only draft returns can be received."
            )

        for item in sales_return.items.all():

            location = item.location

            StockService.increase_stock(
                warehouse=location.warehouse,
                product=item.product,
                quantity=item.quantity,
            )

            StockTransactionService.sales_return(
                product=item.product,
                warehouse=location.warehouse,
                quantity=item.quantity,
                reference_number=sales_return.return_number,
                location=location,
                created_by=received_by,
            )

        sales_return.status = "RECEIVED"
        sales_return.save()

        return sales_return

    @staticmethod
    @transaction.atomic
    def approve(
        sales_return,
        approved_by,
    ):
        """
        Approve Sales Return.
        """

        if sales_return.status != "RECEIVED":
            raise ValueError(
                "Only received returns can be approved."
            )

        sales_return.approved_by = approved_by
        sales_return.status = "APPROVED"
        sales_return.save()

        return sales_return

    @staticmethod
    @transaction.atomic
    def refund(sales_return):
        """
        Mark refund completed.
        """

        if sales_return.status != "APPROVED":
            raise ValueError(
                "Sales Return must be approved."
            )

        SalesReturnService.calculate_total(
            sales_return
        )

        sales_return.status = "REFUNDED"
        sales_return.save()

        return sales_return

    @staticmethod
    @transaction.atomic
    def reject(sales_return):
        """
        Reject Sales Return.
        """

        if sales_return.status == "REFUNDED":
            raise ValueError(
                "Refund already completed."
            )

        sales_return.status = "REJECTED"
        sales_return.save()

        return sales_return