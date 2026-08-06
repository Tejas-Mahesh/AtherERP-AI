from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.sales.models import (
    Customer,
    Quotation,
)


class QuotationAPITest(APITestCase):
    """
    API tests for Quotation endpoints.
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

        self.list_url = reverse(
            "quotation-list",
        )

        self.detail_url = reverse(
            "quotation-detail",
            args=[self.quotation.id],
        )

        self.payload = {
            "quotation_number": "QT0002",
            "customer": self.customer.id,
            "status": "DRAFT",
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_quotations(self):

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

    def test_retrieve_quotation(self):

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

    def test_create_quotation(self):

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
            Quotation.objects.filter(
                quotation_number="QT0002",
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_quotation(self):

        response = self.client.patch(
            self.detail_url,
            {
                "status": "SUBMITTED",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def test_delete_quotation(self):

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

    def test_search_quotation(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "QT0001",
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
                "ordering": "-quotation_date",
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