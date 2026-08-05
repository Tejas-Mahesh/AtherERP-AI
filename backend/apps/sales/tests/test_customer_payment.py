from decimal import Decimal

from django.test import TestCase

from apps.sales.models import (
    Customer,
    SalesOrder,
    SalesInvoice,
    CustomerPayment,
)


class CustomerPaymentModelTest(TestCase):
    """
    Tests for Customer Payment model.
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
            paid_amount=Decimal("0.00"),
            balance_amount=Decimal("50000.00"),
            status="UNPAID",
        )

        self.payment = CustomerPayment.objects.create(
            payment_number="PAY0001",
            customer=self.customer,
            sales_invoice=self.invoice,
            amount=Decimal("10000.00"),
            payment_method="BANK_TRANSFER",
            status="COMPLETED",
            reference_number="TXN123456",
        )

    def test_payment_created(self):

        self.assertEqual(
            self.payment.payment_number,
            "PAY0001",
        )

        self.assertEqual(
            self.payment.customer,
            self.customer,
        )

        self.assertEqual(
            self.payment.sales_invoice,
            self.invoice,
        )

    def test_payment_amount(self):

        self.assertEqual(
            self.payment.amount,
            Decimal("10000.00"),
        )

    def test_payment_status(self):

        self.assertEqual(
            self.payment.status,
            "COMPLETED",
        )

    def test_payment_method(self):

        self.assertEqual(
            self.payment.payment_method,
            "BANK_TRANSFER",
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.payment),
            "PAY0001",
        )