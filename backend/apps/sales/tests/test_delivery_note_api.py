from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.sales.models import (
    Customer,
    SalesOrder,
    DeliveryNote,
)


class DeliveryNoteAPITest(APITestCase):
    """
    API tests for Delivery Note endpoints.
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
            status="PROCESSING",
        )

        self.delivery_note = DeliveryNote.objects.create(
            delivery_number="DN0001",
            sales_order=self.sales_order,
            status="DRAFT",
        )

        self.list_url = reverse(
            "delivery-note-list",
        )

        self.detail_url = reverse(
            "delivery-note-detail",
            args=[self.delivery_note.id],
        )

        self.payload = {
            "delivery_number": "DN0002",
            "sales_order": self.sales_order.id,
            "status": "DRAFT",
        }

    # ----------------------------------
    # LIST
    # ----------------------------------

    def test_list_delivery_notes(self):

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

    def test_retrieve_delivery_note(self):

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

    def test_create_delivery_note(self):

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
            DeliveryNote.objects.filter(
                delivery_number="DN0002",
            ).exists()
        )

    # ----------------------------------
    # UPDATE
    # ----------------------------------

    def test_update_delivery_note(self):

        response = self.client.patch(
            self.detail_url,
            {
                "status": "DELIVERED",
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

    def test_delete_delivery_note(self):

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

    def test_search_delivery_note(self):

        response = self.client.get(
            self.list_url,
            {
                "search": "DN0001",
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
                "ordering": "-delivery_date",
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