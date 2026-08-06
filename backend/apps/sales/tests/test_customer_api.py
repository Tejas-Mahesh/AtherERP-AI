from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from apps.sales.models import Customer


class CustomerAPITest(APITestCase):
    """
    API tests for Customer endpoints.
    """

    def setUp(self):

        self.list_url = reverse(
            "customer-list"
        )

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
            is_active=True,
        )

        self.detail_url = reverse(
            "customer-detail",
            args=[self.customer.id],
        )

        self.payload = {
            "customer_code": "CUST002",
            "name": "XYZ Pvt Ltd",
            "email": "xyz@example.com",
            "phone_number": "9999999999",
            "is_active": True,
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_customers(self):

        response = self.client.get(
            self.list_url
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # RETRIEVE
    # ----------------------------------

    def test_retrieve_customer(self):

        response = self.client.get(
            self.detail_url
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # CREATE
    # ----------------------------------

    def test_create_customer(self):

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
            Customer.objects.filter(
                customer_code="CUST002"
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_customer(self):

        response = self.client.patch(
            self.detail_url,
            {
                "name": "Updated Customer",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.customer.refresh_from_db()

        self.assertEqual(
            self.customer.name,
            "Updated Customer",
        )

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def test_delete_customer(self):

        response = self.client.delete(
            self.detail_url
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

    # ----------------------------------
    # SEARCH
    # ----------------------------------

    def test_search_customer(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "ABC",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # FILTER
    # ----------------------------------

    def test_filter_active_customer(self):

        response = self.client.get(
            self.list_url,
            {
                "is_active": True,
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
                "ordering": "name",
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

        payload = {
            "name": "",
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )