from django.db import transaction
from django.utils import timezone

from apps.sales.models import SalesOrder


class SalesOrderService:
    """
    Sales Order business logic.
    """

    @staticmethod
    def validate_sales_order_number(number):
        """
        Validate Sales Order Number.
        """

        exists = SalesOrder.objects.filter(
            sales_order_number=number
        ).exists()

        if exists:
            raise ValueError(
                "Sales Order number already exists."
            )

    @staticmethod
    @transaction.atomic
    def create_sales_order(**validated_data):
        """
        Create Sales Order.
        """

        SalesOrderService.validate_sales_order_number(
            validated_data["sales_order_number"]
        )

        return SalesOrder.objects.create(
            **validated_data
        )

    @staticmethod
    @transaction.atomic
    def calculate_totals(order):
        """
        Calculate Sales Order totals.
        """

        subtotal = 0
        tax = 0
        discount = 0

        for item in order.items.all():

            subtotal += (
                item.unit_price * item.quantity
            )

            tax += item.tax_amount
            discount += item.discount_amount

        order.subtotal = subtotal
        order.tax_amount = tax
        order.discount_amount = discount

        order.total_amount = (
            subtotal
            + tax
            - discount
        )

        order.save()

        return order

    @staticmethod
    @transaction.atomic
    def submit(order):
        """
        Submit Sales Order.
        """

        if order.status != "DRAFT":
            raise ValueError(
                "Only draft Sales Orders can be submitted."
            )

        order.status = "CONFIRMED"
        order.save()

        return order

    @staticmethod
    @transaction.atomic
    def approve(
        order,
        approved_by,
    ):
        """
        Approve Sales Order.
        """

        if order.status != "CONFIRMED":
            raise ValueError(
                "Only confirmed Sales Orders can be approved."
            )

        order.approved_by = approved_by
        order.approved_at = timezone.now()

        order.status = "PROCESSING"

        order.save()

        return order

    @staticmethod
    @transaction.atomic
    def cancel(order):
        """
        Cancel Sales Order.
        """

        if order.status == "COMPLETED":
            raise ValueError(
                "Completed Sales Orders cannot be cancelled."
            )

        order.status = "CANCELLED"
        order.save()

        return order

    @staticmethod
    @transaction.atomic
    def mark_processing(order):
        """
        Move order to Processing.
        """

        if order.status != "CONFIRMED":
            raise ValueError(
                "Sales Order must be confirmed."
            )

        order.status = "PROCESSING"
        order.save()

        return order