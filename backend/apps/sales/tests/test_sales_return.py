from decimal import Decimal

from django.test import TestCase

from apps.sales.models import (
    Customer,
    SalesOrder,
    SalesInvoice,
    SalesReturn,
)


class SalesReturnModelTest(TestCase):
    """
    Tests for Sales Return model.
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
            total_amount=Decimal("50000.00"),
            paid_amount=Decimal("50000.00"),
            balance_amount=Decimal("0.00"),
            status="PAID",
        )

        self.sales_return = SalesReturn.objects.create(
            return_number="SR0001",
            customer=self.customer,
            sales_invoice=self.invoice,
            total_amount=Decimal("5000.00"),
            status="COMPLETED",
            reason="Damaged Product",
        )

    def test_sales_return_created(self):

        self.assertEqual(
            self.sales_return.return_number,
            "SR0001",
        )

        self.assertEqual(
            self.sales_return.customer,
            self.customer,
        )

        self.assertEqual(
            self.sales_return.sales_invoice,
            self.invoice,
        )

    def test_return_amount(self):

        self.assertEqual(
            self.sales_return.total_amount,
            Decimal("5000.00"),
        )

    def test_return_status(self):

        self.assertEqual(
            self.sales_return.status,
            "COMPLETED",
        )

    def test_return_reason(self):

        self.assertEqual(
            self.sales_return.reason,
            "Damaged Product",
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.sales_return),
            "SR0001",
        )