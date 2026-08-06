from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.sales.models import (
    Customer,
    SalesInvoice,
)


class SalesInvoiceAPITest(APITestCase):
    """
    API tests for Sales Invoice endpoints.
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

        self.list_url = reverse(
            "sales-invoice-list",
        )

        self.detail_url = reverse(
            "sales-invoice-detail",
            args=[self.invoice.id],
        )

        self.payload = {
            "invoice_number": "INV0002",
            "customer": self.customer.id,
            "total_amount": "500.00",
            "paid_amount": "0.00",
            "balance_amount": "500.00",
            "status": "DRAFT",
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_sales_invoices(self):

        response = self.client.get(
            self.list_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # RETRIEVE
    # ----------------------------------

    def test_retrieve_sales_invoice(self):

        response = self.client.get(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # CREATE
    # ----------------------------------

    def test_create_sales_invoice(self):

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            SalesInvoice.objects.filter(
                invoice_number="INV0002",
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_sales_invoice(self):

        response = self.client.patch(
            self.detail_url,
            {
                "status": "ISSUED",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.invoice.refresh_from_db()

        self.assertEqual(
            self.invoice.status,
            "ISSUED",
        )

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def test_delete_sales_invoice(self):

        response = self.client.delete(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

    # ----------------------------------
    # SEARCH
    # ----------------------------------

    def test_search_sales_invoice(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "INV0001",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # FILTER
    # ----------------------------------

    def test_filter_status(self):

        response = self.client.get(
            self.list_url,
            {
                "status": "DRAFT",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # ORDERING
    # ----------------------------------

    def test_ordering(self):

        response = self.client.get(
            self.list_url,
            {
                "ordering": "-invoice_date",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # INVALID CREATE
    # ----------------------------------

    def test_invalid_create(self):

        response = self.client.post(
            self.list_url,
            {},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )