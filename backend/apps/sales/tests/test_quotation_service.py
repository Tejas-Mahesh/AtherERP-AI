from django.test import TestCase

from apps.sales.models import (
    Customer,
    Quotation,
    SalesOrder,
)
from apps.sales.services import QuotationService


class QuotationServiceTest(TestCase):
    """
    Tests for QuotationService.
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
            status="DRAFT",
        )

    # ------------------------------------
    # validate_quotation_number()
    # ------------------------------------

    def test_validate_unique_number(self):

        QuotationService.validate_quotation_number(
            "QT9999"
        )

    def test_validate_duplicate_number(self):

        with self.assertRaises(ValueError):

            QuotationService.validate_quotation_number(
                "QT0001"
            )

    # ------------------------------------
    # create_quotation()
    # ------------------------------------

    def test_create_quotation(self):

        quotation = (
            QuotationService.create_quotation(
                quotation_number="QT0002",
                customer=self.customer,
                status="DRAFT",
            )
        )

        self.assertEqual(
            quotation.quotation_number,
            "QT0002",
        )

    def test_create_duplicate_quotation(self):

        with self.assertRaises(ValueError):

            QuotationService.create_quotation(
                quotation_number="QT0001",
                customer=self.customer,
            )

    # ------------------------------------
    # submit()
    # ------------------------------------

    def test_submit_quotation(self):

        quotation = QuotationService.submit(
            self.quotation
        )

        self.assertEqual(
            quotation.status,
            "SUBMITTED",
        )

    def test_submit_non_draft(self):

        self.quotation.status = "APPROVED"

        self.quotation.save()

        with self.assertRaises(ValueError):

            QuotationService.submit(
                self.quotation
            )

    # ------------------------------------
    # approve()
    # ------------------------------------

    def test_approve_quotation(self):

        self.quotation.status = "SUBMITTED"

        self.quotation.save()

        quotation = QuotationService.approve(
            self.quotation
        )

        self.assertEqual(
            quotation.status,
            "APPROVED",
        )

    def test_approve_invalid_status(self):

        with self.assertRaises(ValueError):

            QuotationService.approve(
                self.quotation
            )

    # ------------------------------------
    # reject()
    # ------------------------------------

    def test_reject_quotation(self):

        quotation = QuotationService.reject(
            self.quotation
        )

        self.assertEqual(
            quotation.status,
            "REJECTED",
        )

    # ------------------------------------
    # expire()
    # ------------------------------------

    def test_expire_quotation(self):

        quotation = QuotationService.expire(
            self.quotation
        )

        self.assertEqual(
            quotation.status,
            "EXPIRED",
        )

    # ------------------------------------
    # convert_to_sales_order()
    # ------------------------------------

    def test_convert_to_sales_order(self):

        self.quotation.status = "APPROVED"

        self.quotation.save()

        sales_order = (
            QuotationService.convert_to_sales_order(
                quotation=self.quotation,
                sales_order_number="SO0001",
            )
        )

        self.assertIsInstance(
            sales_order,
            SalesOrder,
        )

        self.assertEqual(
            sales_order.sales_order_number,
            "SO0001",
        )

        self.quotation.refresh_from_db()

        self.assertEqual(
            self.quotation.status,
            "CONVERTED",
        )

    def test_convert_without_approval(self):

        with self.assertRaises(ValueError):

            QuotationService.convert_to_sales_order(
                quotation=self.quotation,
                sales_order_number="SO0001",
            )