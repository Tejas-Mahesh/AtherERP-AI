from decimal import Decimal

from django.test import TestCase

from apps.sales.models import (
    Customer,
    SalesOrder,
    SalesInvoice,
)


class SalesInvoiceModelTest(TestCase):
    """
    Tests for Sales Invoice model.
    """

    def setUp(self):

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
        )

        self.sales_order = SalesOrder.objects.create(
            sales_order_number="SO0001",
            customer=self.customer,
            status="COMPLETED",
        )

        self.invoice = SalesInvoice.objects.create(
            invoice_number="INV0001",
            customer=self.customer,
            sales_order=self.sales_order,
            subtotal=Decimal("50000.00"),
            tax_amount=Decimal("9000.00"),
            discount_amount=Decimal("1000.00"),
            total_amount=Decimal("58000.00"),
            paid_amount=Decimal("0.00"),
            balance_amount=Decimal("58000.00"),
            status="UNPAID",
        )

    def test_invoice_created(self):

        self.assertEqual(
            self.invoice.invoice_number,
            "INV0001",
        )

        self.assertEqual(
            self.invoice.customer,
            self.customer,
        )

        self.assertEqual(
            self.invoice.sales_order,
            self.sales_order,
        )

        self.assertEqual(
            self.invoice.status,
            "UNPAID",
        )

    def test_total_amount(self):

        self.assertEqual(
            self.invoice.total_amount,
            Decimal("58000.00"),
        )

    def test_balance_amount(self):

        self.assertEqual(
            self.invoice.balance_amount,
            Decimal("58000.00"),
        )

    def test_paid_amount(self):

        self.assertEqual(
            self.invoice.paid_amount,
            Decimal("0.00"),
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.invoice),
            "INV0001",
        )