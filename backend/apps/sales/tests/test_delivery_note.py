from django.test import TestCase

from apps.organizations.models import Organization
from apps.inventory.models import Warehouse
from apps.sales.models import (
    Customer,
    SalesOrder,
    DeliveryNote,
)


class DeliveryNoteModelTest(TestCase):
    """
    Tests for Delivery Note model.
    """

    def setUp(self):

        self.organization = Organization.objects.create(
            name="ABC Technologies",
        )

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
        )

        self.sales_order = SalesOrder.objects.create(
            sales_order_number="SO0001",
            customer=self.customer,
            status="APPROVED",
        )

        self.warehouse = Warehouse.objects.create(
            organization=self.organization,
            name="Main Warehouse",
            code="WH001",
            address="Bangalore",
            city="Bangalore",
            state="Karnataka",
            country="India",
            postal_code="560001",
        )

        self.delivery_note = DeliveryNote.objects.create(
            delivery_number="DN0001",
            sales_order=self.sales_order,
            warehouse=self.warehouse,
            status="DRAFT",
        )

    def test_delivery_note_created(self):

        self.assertEqual(
            self.delivery_note.delivery_number,
            "DN0001",
        )

        self.assertEqual(
            self.delivery_note.sales_order,
            self.sales_order,
        )

        self.assertEqual(
            self.delivery_note.warehouse,
            self.warehouse,
        )

        self.assertEqual(
            self.delivery_note.status,
            "DRAFT",
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.delivery_note),
            "DN0001",
        )