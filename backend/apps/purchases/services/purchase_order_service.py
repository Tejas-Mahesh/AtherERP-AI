from decimal import Decimal

from django.db import transaction
from django.utils import timezone

from apps.purchases.models import PurchaseOrder


class PurchaseOrderService:
    """
    Purchase Order Business Logic.

    Responsible for:

    - Validation
    - Creation
    - Total Calculation
    - Submit
    - Approve
    - Mark Ordered
    - Cancel
    """

    # =====================================================
    # Validation
    # =====================================================

    @staticmethod
    def validate_purchase_number(number):
        """
        Ensure purchase number is unique.
        """

        if PurchaseOrder.objects.filter(
            purchase_number=number
        ).exists():
            raise ValueError(
                "Purchase number already exists."
            )

    @staticmethod
    def validate_supplier(supplier):
        """
        Supplier must be active.
        """

        if not supplier.is_active:
            raise ValueError(
                "Supplier is inactive."
            )

    # =====================================================
    # Create Purchase Order
    # =====================================================

    @staticmethod
    @transaction.atomic
    def create_purchase_order(**validated_data):
        """
        Create Purchase Order.
        """

        PurchaseOrderService.validate_purchase_number(
            validated_data["purchase_number"]
        )

        PurchaseOrderService.validate_supplier(
            validated_data["supplier"]
        )

        return PurchaseOrder.objects.create(
            **validated_data
        )

    # =====================================================
    # Calculate Totals
    # =====================================================

    @staticmethod
    @transaction.atomic
    def calculate_totals(po):
        """
        Recalculate Purchase Order totals.
        """

        subtotal = Decimal("0.00")
        tax_amount = Decimal("0.00")
        discount_amount = Decimal("0.00")

        for item in po.items.all():

            subtotal += (
                item.unit_price *
                item.quantity
            )

            tax_amount += item.tax_amount
            discount_amount += item.discount_amount

        po.subtotal = subtotal
        po.tax_amount = tax_amount
        po.discount_amount = discount_amount

        po.total_amount = (
            subtotal
            + tax_amount
            - discount_amount
        )

        po.save(
            update_fields=[
                "subtotal",
                "tax_amount",
                "discount_amount",
                "total_amount",
            ]
        )

        return po

    # =====================================================
    # Submit
    # =====================================================

    @staticmethod
    @transaction.atomic
    def submit(po):

        if po.status != "DRAFT":
            raise ValueError(
                "Only draft Purchase Orders can be submitted."
            )

        PurchaseOrderService.calculate_totals(po)

        po.status = "SUBMITTED"

        po.save(
            update_fields=[
                "status",
            ]
        )

        return po

    # =====================================================
    # Approve
    # =====================================================

    @staticmethod
    @transaction.atomic
    def approve(
        po,
        approved_by,
    ):

        if po.status != "SUBMITTED":
            raise ValueError(
                "Only submitted Purchase Orders can be approved."
            )

        po.status = "APPROVED"
        po.approved_by = approved_by
        po.approved_at = timezone.now()

        po.save(
            update_fields=[
                "status",
                "approved_by",
                "approved_at",
            ]
        )

        return po

    # =====================================================
    # Mark Ordered
    # =====================================================

    @staticmethod
    @transaction.atomic
    def mark_ordered(po):

        if po.status != "APPROVED":
            raise ValueError(
                "Purchase Order must be approved first."
            )

        po.status = "ORDERED"

        po.save(
            update_fields=[
                "status",
            ]
        )

        return po

    # =====================================================
    # Cancel
    # =====================================================

    @staticmethod
    @transaction.atomic
    def cancel(po):

        if po.status == "COMPLETED":
            raise ValueError(
                "Completed Purchase Orders cannot be cancelled."
            )

        po.status = "CANCELLED"

        po.save(
            update_fields=[
                "status",
            ]
        )

        return po

    # =====================================================
    # Reopen
    # =====================================================

    @staticmethod
    @transaction.atomic
    def reopen(po):

        if po.status != "CANCELLED":
            raise ValueError(
                "Only cancelled Purchase Orders can be reopened."
            )

        po.status = "DRAFT"

        po.save(
            update_fields=[
                "status",
            ]
        )

        return po

    # =====================================================
    # Helper Methods
    # =====================================================

    @staticmethod
    def total_items(po):
        """
        Returns total line items.
        """

        return po.items.count()

    @staticmethod
    def total_quantity(po):
        """
        Returns total ordered quantity.
        """

        return sum(
            item.quantity
            for item in po.items.all()
        )

    @staticmethod
    def total_received_quantity(po):
        """
        Returns total received quantity.
        """

        return sum(
            item.received_quantity
            for item in po.items.all()
        )