from decimal import Decimal

from django.db import transaction

from apps.sales.models import SalesInvoice


class InvoiceService:
    """
    Business logic for Sales Invoice.
    """

    @staticmethod
    def validate_invoice_number(number):
        """
        Validate invoice number uniqueness.
        """

        exists = SalesInvoice.objects.filter(
            invoice_number=number
        ).exists()

        if exists:
            raise ValueError(
                "Invoice number already exists."
            )

    @staticmethod
    @transaction.atomic
    def create_invoice(**validated_data):
        """
        Create Sales Invoice.
        """

        InvoiceService.validate_invoice_number(
            validated_data["invoice_number"]
        )

        return SalesInvoice.objects.create(
            **validated_data
        )

    @staticmethod
    @transaction.atomic
    def calculate_totals(invoice):
        """
        Calculate invoice totals.
        """

        subtotal = Decimal("0.00")
        tax = Decimal("0.00")
        discount = Decimal("0.00")

        for item in invoice.items.all():

            subtotal += (
                item.unit_price * item.quantity
            )

            tax += item.tax_amount
            discount += item.discount_amount

        invoice.subtotal = subtotal
        invoice.tax_amount = tax
        invoice.discount_amount = discount

        invoice.total_amount = (
            subtotal
            + tax
            - discount
        )

        invoice.balance_amount = (
            invoice.total_amount
            - invoice.paid_amount
        )

        invoice.save()

        return invoice

    @staticmethod
    @transaction.atomic
    def issue(invoice):
        """
        Issue invoice.
        """

        if invoice.status != "DRAFT":
            raise ValueError(
                "Only draft invoices can be issued."
            )

        invoice.status = "ISSUED"
        invoice.save()

        return invoice

    @staticmethod
    @transaction.atomic
    def record_payment(
        invoice,
        amount,
    ):
        """
        Update invoice after payment.
        """

        invoice.paid_amount += amount

        invoice.balance_amount = (
            invoice.total_amount
            - invoice.paid_amount
        )

        if invoice.balance_amount <= 0:

            invoice.status = "PAID"

        elif invoice.paid_amount > 0:

            invoice.status = "PARTIALLY_PAID"

        invoice.save()

        return invoice

    @staticmethod
    @transaction.atomic
    def cancel(invoice):
        """
        Cancel invoice.
        """

        if invoice.paid_amount > 0:
            raise ValueError(
                "Cannot cancel a paid invoice."
            )

        invoice.status = "CANCELLED"
        invoice.save()

        return invoice