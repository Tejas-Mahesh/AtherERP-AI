from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.sales.models import (
    Customer,
    SalesInvoice,
    SalesReturn,
)


class SalesReturnAPITest(APITestCase):
    """
    API tests for Sales Return endpoints.
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
            paid_amount=Decimal("1000.00"),
            balance_amount=Decimal("0.00"),
            status="PAID",
        )

        self.sales_return = SalesReturn.objects.create(
            return_number="SR0001",
            customer=self.customer,
            sales_invoice=self.invoice,
            status="DRAFT",
        )

        self.list_url = reverse(
            "sales-return-list",
        )

        self.detail_url = reverse(
            "sales-return-detail",
            args=[self.sales_return.id],
        )

        self.payload = {
            "return_number": "SR0002",
            "customer": self.customer.id,
            "sales_invoice": self.invoice.id,
            "status": "DRAFT",
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_sales_returns(self):

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

    def test_retrieve_sales_return(self):

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

    def test_create_sales_return(self):

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
            SalesReturn.objects.filter(
                return_number="SR0002",
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_sales_return(self):

        response = self.client.patch(
            self.detail_url,
            {
                "status": "RECEIVED",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.sales_return.refresh_from_db()

        self.assertEqual(
            self.sales_return.status,
            "RECEIVED",
        )

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def test_delete_sales_return(self):

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

    def test_search_sales_return(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "SR0001",
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
                "ordering": "-return_date",
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