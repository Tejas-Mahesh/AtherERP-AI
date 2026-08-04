from django.db import transaction

from apps.sales.models import CustomerPayment
from apps.sales.services.invoice_service import InvoiceService


class PaymentService:
    """
    Customer Payment business logic.
    """

    @staticmethod
    def validate_payment_number(number):
        """
        Ensure payment number is unique.
        """

        exists = CustomerPayment.objects.filter(
            payment_number=number
        ).exists()

        if exists:
            raise ValueError(
                "Payment number already exists."
            )

    @staticmethod
    def validate_payment(invoice, amount):
        """
        Validate payment amount.
        """

        if amount <= 0:
            raise ValueError(
                "Payment amount must be greater than zero."
            )

        if amount > invoice.balance_amount:
            raise ValueError(
                "Payment exceeds outstanding balance."
            )

    @staticmethod
    @transaction.atomic
    def create_payment(**validated_data):
        """
        Create customer payment.
        """

        invoice = validated_data["sales_invoice"]
        amount = validated_data["amount"]

        PaymentService.validate_payment_number(
            validated_data["payment_number"]
        )

        PaymentService.validate_payment(
            invoice,
            amount,
        )

        payment = CustomerPayment.objects.create(
            **validated_data
        )

        InvoiceService.record_payment(
            invoice,
            amount,
        )

        return payment

    @staticmethod
    @transaction.atomic
    def cancel_payment(payment):
        """
        Cancel customer payment.
        """

        if payment.status == "CANCELLED":
            raise ValueError(
                "Payment is already cancelled."
            )

        invoice = payment.sales_invoice

        invoice.paid_amount -= payment.amount

        if invoice.paid_amount < 0:
            invoice.paid_amount = 0

        invoice.balance_amount = (
            invoice.total_amount
            - invoice.paid_amount
        )

        if invoice.paid_amount == 0:

            invoice.status = "ISSUED"

        elif invoice.balance_amount > 0:

            invoice.status = "PARTIALLY_PAID"

        else:

            invoice.status = "PAID"

        invoice.save()

        payment.status = "CANCELLED"
        payment.save()

        return payment