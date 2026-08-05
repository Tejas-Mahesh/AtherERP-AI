from decimal import Decimal

from django.test import TestCase

from apps.sales.models import (
    Customer,
    SalesInvoice,
)
from apps.sales.services import (
    InvoiceService,
)


class InvoiceServiceTest(TestCase):
    """
    Tests for InvoiceService.
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
            status="DRAFT",
        )

    # ------------------------------------
    # validate_invoice_number()
    # ------------------------------------

    def test_validate_unique_invoice_number(self):

        InvoiceService.validate_invoice_number(
            "INV9999",
        )

    def test_validate_duplicate_invoice_number(self):

        with self.assertRaises(
            ValueError,
        ):

            InvoiceService.validate_invoice_number(
                "INV0001",
            )

    # ------------------------------------
    # create_invoice()
    # ------------------------------------

    def test_create_invoice(self):

        invoice = InvoiceService.create_invoice(
            invoice_number="INV0002",
            customer=self.customer,
            total_amount=Decimal("500.00"),
            paid_amount=Decimal("0.00"),
            balance_amount=Decimal("500.00"),
            status="DRAFT",
        )

        self.assertEqual(
            invoice.invoice_number,
            "INV0002",
        )

    def test_create_duplicate_invoice(self):

        with self.assertRaises(
            ValueError,
        ):

            InvoiceService.create_invoice(
                invoice_number="INV0001",
                customer=self.customer,
            )

    # ------------------------------------
    # issue()
    # ------------------------------------

    def test_issue_invoice(self):

        invoice = InvoiceService.issue(
            self.invoice,
        )

        self.assertEqual(
            invoice.status,
            "ISSUED",
        )

    def test_issue_non_draft_invoice(self):

        self.invoice.status = "PAID"

        self.invoice.save()

        with self.assertRaises(
            ValueError,
        ):

            InvoiceService.issue(
                self.invoice,
            )

    # ------------------------------------
    # record_payment()
    # ------------------------------------

    def test_partial_payment(self):

        invoice = InvoiceService.record_payment(
            self.invoice,
            Decimal("400.00"),
        )

        self.assertEqual(
            invoice.paid_amount,
            Decimal("400.00"),
        )

        self.assertEqual(
            invoice.balance_amount,
            Decimal("600.00"),
        )

        self.assertEqual(
            invoice.status,
            "PARTIALLY_PAID",
        )

    def test_full_payment(self):

        invoice = InvoiceService.record_payment(
            self.invoice,
            Decimal("1000.00"),
        )

        self.assertEqual(
            invoice.paid_amount,
            Decimal("1000.00"),
        )

        self.assertEqual(
            invoice.balance_amount,
            Decimal("0.00"),
        )

        self.assertEqual(
            invoice.status,
            "PAID",
        )

    # ------------------------------------
    # cancel()
    # ------------------------------------

    def test_cancel_invoice(self):

        invoice = InvoiceService.cancel(
            self.invoice,
        )

        self.assertEqual(
            invoice.status,
            "CANCELLED",
        )

    def test_cancel_paid_invoice(self):

        self.invoice.paid_amount = Decimal("100.00")

        self.invoice.save()

        with self.assertRaises(
            ValueError,
        ):

            InvoiceService.cancel(
                self.invoice,
            )