from django.test import TestCase

from apps.sales.models import Customer
from apps.sales.services import CustomerService


class CustomerServiceTest(TestCase):
    """
    Tests for CustomerService.
    """

    def setUp(self):

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
            is_active=True,
        )

    # ------------------------------------
    # validate_customer()
    # ------------------------------------

    def test_validate_active_customer(self):

        customer = CustomerService.validate_customer(
            self.customer
        )

        self.assertEqual(
            customer,
            self.customer,
        )

    def test_validate_inactive_customer(self):

        self.customer.is_active = False

        self.customer.save()

        with self.assertRaises(
            ValueError,
        ):

            CustomerService.validate_customer(
                self.customer
            )

    # ------------------------------------
    # validate_customer_code()
    # ------------------------------------

    def test_validate_unique_customer_code(self):

        CustomerService.validate_customer_code(
            "CUST999"
        )

    def test_validate_duplicate_customer_code(self):

        with self.assertRaises(
            ValueError,
        ):

            CustomerService.validate_customer_code(
                "CUST001"
            )

    # ------------------------------------
    # create_customer()
    # ------------------------------------

    def test_create_customer(self):

        customer = CustomerService.create_customer(
            customer_code="CUST002",
            name="XYZ Pvt Ltd",
            email="xyz@example.com",
            phone_number="9999999999",
        )

        self.assertEqual(
            customer.customer_code,
            "CUST002",
        )

        self.assertEqual(
            customer.name,
            "XYZ Pvt Ltd",
        )

        self.assertTrue(
            Customer.objects.filter(
                customer_code="CUST002"
            ).exists()
        )

    def test_create_customer_duplicate_code(self):

        with self.assertRaises(
            ValueError,
        ):

            CustomerService.create_customer(
                customer_code="CUST001",
                name="Duplicate",
                email="duplicate@example.com",
                phone_number="9999999999",
            )

    # ------------------------------------
    # activate_customer()
    # ------------------------------------

    def test_activate_customer(self):

        self.customer.is_active = False

        self.customer.save()

        customer = (
            CustomerService.activate_customer(
                self.customer
            )
        )

        self.assertTrue(
            customer.is_active
        )

    # ------------------------------------
    # deactivate_customer()
    # ------------------------------------

    def test_deactivate_customer(self):

        customer = (
            CustomerService.deactivate_customer(
                self.customer
            )
        )

        self.assertFalse(
            customer.is_active
        )