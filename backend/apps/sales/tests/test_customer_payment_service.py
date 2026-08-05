from decimal import Decimal
from unittest.mock import patch

from django.test import TestCase

from apps.sales.models import (
    Customer,
    SalesInvoice,
    CustomerPayment,
)
from apps.sales.services import (
    PaymentService,
)


class PaymentServiceTest(TestCase):
    """
    Tests for PaymentService.
    """

    def setUp(self):

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
        )

        self.invoice = SalesInvoice.objects.create(
            invoice_number="INV0001",
            customer=self.customer,
            total_amount=Decimal("1000.00"),
            paid_amount=Decimal("0.00"),
            balance_amount=Decimal("1000.00"),
            status="ISSUED",
        )

        self.payment = CustomerPayment.objects.create(
            payment_number="PAY0001",
            customer=self.customer,
            sales_invoice=self.invoice,
            amount=Decimal("200.00"),
            status="COMPLETED",
        )

    # ------------------------------------
    # validate_payment_number()
    # ------------------------------------

    def test_validate_unique_payment_number(self):

        PaymentService.validate_payment_number(
            "PAY9999",
        )

    def test_validate_duplicate_payment_number(self):

        with self.assertRaises(
            ValueError,
        ):

            PaymentService.validate_payment_number(
                "PAY0001",
            )

    # ------------------------------------
    # validate_payment()
    # ------------------------------------

    def test_validate_payment_success(self):

        PaymentService.validate_payment(
            self.invoice,
            Decimal("500.00"),
        )

    def test_validate_negative_payment(self):

        with self.assertRaises(
            ValueError,
        ):

            PaymentService.validate_payment(
                self.invoice,
                Decimal("-10.00"),
            )

    def test_validate_zero_payment(self):

        with self.assertRaises(
            ValueError,
        ):

            PaymentService.validate_payment(
                self.invoice,
                Decimal("0.00"),
            )

    def test_validate_excess_payment(self):

        with self.assertRaises(
            ValueError,
        ):

            PaymentService.validate_payment(
                self.invoice,
                Decimal("5000.00"),
            )

    # ------------------------------------
    # create_payment()
    # ------------------------------------

    @patch(
        "apps.sales.services.payment_service.InvoiceService.record_payment"
    )
    def test_create_payment(
        self,
        mock_record_payment,
    ):

        payment = PaymentService.create_payment(
            payment_number="PAY0002",
            customer=self.customer,
            sales_invoice=self.invoice,
            amount=Decimal("300.00"),
            status="COMPLETED",
        )

        self.assertEqual(
            payment.payment_number,
            "PAY0002",
        )

        mock_record_payment.assert_called_once_with(
            self.invoice,
            Decimal("300.00"),
        )

    # ------------------------------------
    # cancel_payment()
    # ------------------------------------

    def test_cancel_payment(self):

        self.invoice.paid_amount = Decimal("200.00")
        self.invoice.balance_amount = Decimal("800.00")
        self.invoice.status = "PARTIALLY_PAID"
        self.invoice.save()

        payment = (
            PaymentService.cancel_payment(
                self.payment,
            )
        )

        self.assertEqual(
            payment.status,
            "CANCELLED",
        )

        self.invoice.refresh_from_db()

        self.assertEqual(
            self.invoice.paid_amount,
            Decimal("0.00"),
        )

        self.assertEqual(
            self.invoice.balance_amount,
            Decimal("1000.00"),
        )

        self.assertEqual(
            self.invoice.status,
            "ISSUED",
        )

    def test_cancel_already_cancelled_payment(self):

        self.payment.status = "CANCELLED"
        self.payment.save()

        with self.assertRaises(
            ValueError,
        ):

            PaymentService.cancel_payment(
                self.payment,
            )