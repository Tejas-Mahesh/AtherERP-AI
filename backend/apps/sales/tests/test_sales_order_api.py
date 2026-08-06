from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.sales.models import (
    Customer,
    SalesOrder,
)


class SalesOrderAPITest(APITestCase):
    """
    API tests for Sales Order endpoints.
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
            status="DRAFT",
        )

        self.list_url =     reverse("sales-order-list"),
        

        self.detail_url = reverse(
            "sales-order-detail",
            args=[self.sales_order.id],
        )

        self.payload = {
            "sales_order_number": "SO0002",
            "customer": self.customer.id,
            "status": "DRAFT",
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_sales_orders(self):

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

    def test_retrieve_sales_order(self):

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

    def test_create_sales_order(self):

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
            SalesOrder.objects.filter(
                sales_order_number="SO0002",
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_sales_order(self):

        response = self.client.patch(
            self.detail_url,
            {
                "status": "CONFIRMED",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.sales_order.refresh_from_db()

        self.assertEqual(
            self.sales_order.status,
            "CONFIRMED",
        )

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def test_delete_sales_order(self):

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

    def test_search_sales_order(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "SO0001",
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
                "ordering": "-order_date",
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