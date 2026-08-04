from django.db import transaction


class SalesOrderStatusService:
    """
    Handles automatic Sales Order status updates.
    """

    @staticmethod
    @transaction.atomic
    def update_status(sales_order):
        """
        Update Sales Order status based on delivered quantities.
        """

        items = sales_order.items.all()

        if not items.exists():
            sales_order.status = "DRAFT"
            sales_order.save()
            return sales_order

        total_quantity = 0
        delivered_quantity = 0

        for item in items:
            total_quantity += item.quantity
            delivered_quantity += item.delivered_quantity

        if delivered_quantity == 0:

            sales_order.status = "CONFIRMED"

        elif delivered_quantity < total_quantity:

            sales_order.status = "PARTIALLY_DELIVERED"

        else:

            sales_order.status = "COMPLETED"

        sales_order.save()

        return sales_order

    @staticmethod
    @transaction.atomic
    def mark_processing(sales_order):
        """
        Mark Sales Order as Processing.
        """

        if sales_order.status != "CONFIRMED":
            raise ValueError(
                "Only confirmed Sales Orders can be processed."
            )

        sales_order.status = "PROCESSING"
        sales_order.save()

        return sales_order

    @staticmethod
    @transaction.atomic
    def mark_completed(sales_order):
        """
        Mark Sales Order as Completed.
        """

        sales_order.status = "COMPLETED"
        sales_order.save()

        return sales_order

    @staticmethod
    @transaction.atomic
    def cancel(sales_order):
        """
        Cancel Sales Order.
        """

        if sales_order.status == "COMPLETED":
            raise ValueError(
                "Completed Sales Orders cannot be cancelled."
            )

        sales_order.status = "CANCELLED"
        sales_order.save()

        return sales_order