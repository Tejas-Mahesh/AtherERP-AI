from decimal import Decimal

from django.test import TestCase

from apps.sales.models import (
    Customer,
    SalesOrder,
)


class SalesOrderModelTest(TestCase):
    """
    Tests for Sales Order model.
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
            subtotal=Decimal("25000.00"),
            tax_amount=Decimal("4500.00"),
            discount_amount=Decimal("1000.00"),
            total_amount=Decimal("28500.00"),
            status="DRAFT",
        )

    def test_sales_order_created(self):

        self.assertEqual(
            self.sales_order.sales_order_number,
            "SO0001",
        )

        self.assertEqual(
            self.sales_order.customer,
            self.customer,
        )

        self.assertEqual(
            self.sales_order.status,
            "DRAFT",
        )

    def test_total_amount(self):

        self.assertEqual(
            self.sales_order.total_amount,
            Decimal("28500.00"),
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.sales_order),
            "SO0001",
        )