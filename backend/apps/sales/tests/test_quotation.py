from decimal import Decimal

from django.test import TestCase

from apps.sales.models import (
    Customer,
    Quotation,
)


class QuotationModelTest(TestCase):
    """
    Tests for Quotation model.
    """

    def setUp(self):

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
        )

        self.quotation = Quotation.objects.create(
            quotation_number="QT0001",
            customer=self.customer,
            subtotal=Decimal("10000.00"),
            tax_amount=Decimal("1800.00"),
            discount_amount=Decimal("500.00"),
            total_amount=Decimal("11300.00"),
            status="DRAFT",
        )

    def test_quotation_created(self):

        self.assertEqual(
            self.quotation.quotation_number,
            "QT0001",
        )

        self.assertEqual(
            self.quotation.customer,
            self.customer,
        )

        self.assertEqual(
            self.quotation.status,
            "DRAFT",
        )

    def test_total_amount(self):

        self.assertEqual(
            self.quotation.total_amount,
            Decimal("11300.00"),
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.quotation),
            "QT0001",
        )