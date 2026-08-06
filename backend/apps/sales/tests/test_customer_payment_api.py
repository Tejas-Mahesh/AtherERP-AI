from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.sales.models import (
    Customer,
    SalesInvoice,
    CustomerPayment,
)


class CustomerPaymentAPITest(APITestCase):
    """
    API tests for Customer Payment endpoints.
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
            amount=Decimal("250.00"),
            status="COMPLETED",
        )

        self.list_url = reverse(
            "customerpayment-list",
        )

        self.detail_url = reverse(
            "customerpayment-detail",
            args=[self.payment.id],
        )

        self.payload = {
            "payment_number": "PAY0002",
            "customer": self.customer.id,
            "sales_invoice": self.invoice.id,
            "amount": "500.00",
            "status": "COMPLETED",
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_customer_payments(self):

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

    def test_retrieve_customer_payment(self):

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

    def test_create_customer_payment(self):

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
            CustomerPayment.objects.filter(
                payment_number="PAY0002",
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_customer_payment(self):

        response = self.client.patch(
            self.detail_url,
            {
                "status": "CANCELLED",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.payment.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            "CANCELLED",
        )

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def test_delete_customer_payment(self):

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

    def test_search_customer_payment(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "PAY0001",
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
                "status": "COMPLETED",
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
                "ordering": "-payment_date",
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