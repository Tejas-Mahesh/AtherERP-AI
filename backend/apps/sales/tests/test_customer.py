from django.test import TestCase

from apps.sales.models import Customer


class CustomerModelTest(TestCase):
    """
    Tests for Customer model.
    """

    def setUp(self):

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
        )

    def test_customer_created(self):

        self.assertEqual(
            self.customer.customer_code,
            "CUST001",
        )

        self.assertEqual(
            self.customer.name,
            "ABC Technologies",
        )

    def test_string_representation(self):

        self.assertEqual(
            str(self.customer),
            "ABC Technologies",
        )