from django.test import TestCase

from apps.accounts.models import User
from apps.sales.models import (
    Customer,
    SalesOrder,
)
from apps.sales.services import (
    SalesOrderService,
)


class SalesOrderServiceTest(TestCase):
    """
    Tests for SalesOrderService.
    """

    def setUp(self):

        self.customer = Customer.objects.create(
            customer_code="CUST001",
            name="ABC Technologies",
            email="abc@example.com",
            phone_number="9876543210",
        )

        self.user = User.objects.create(
            username="admin",
            email="admin@example.com",
        )

        self.order = SalesOrder.objects.create(
            sales_order_number="SO0001",
            customer=self.customer,
            status="DRAFT",
        )

    # ------------------------------------
    # validate_sales_order_number()
    # ------------------------------------

    def test_validate_unique_sales_order_number(self):

        SalesOrderService.validate_sales_order_number(
            "SO9999",
        )

    def test_validate_duplicate_sales_order_number(self):

        with self.assertRaises(
            ValueError,
        ):

            SalesOrderService.validate_sales_order_number(
                "SO0001",
            )

    # ------------------------------------
    # create_sales_order()
    # ------------------------------------

    def test_create_sales_order(self):

        order = (
            SalesOrderService.create_sales_order(
                sales_order_number="SO0002",
                customer=self.customer,
                status="DRAFT",
            )
        )

        self.assertEqual(
            order.sales_order_number,
            "SO0002",
        )

    def test_create_duplicate_sales_order(self):

        with self.assertRaises(
            ValueError,
        ):

            SalesOrderService.create_sales_order(
                sales_order_number="SO0001",
                customer=self.customer,
            )

    # ------------------------------------
    # submit()
    # ------------------------------------

    def test_submit_sales_order(self):

        order = SalesOrderService.submit(
            self.order,
        )

        self.assertEqual(
            order.status,
            "CONFIRMED",
        )

    def test_submit_non_draft_order(self):

        self.order.status = "PROCESSING"

        self.order.save()

        with self.assertRaises(
            ValueError,
        ):

            SalesOrderService.submit(
                self.order,
            )

    # ------------------------------------
    # approve()
    # ------------------------------------

    def test_approve_sales_order(self):

        self.order.status = "CONFIRMED"

        self.order.save()

        order = SalesOrderService.approve(
            self.order,
            self.user,
        )

        self.assertEqual(
            order.status,
            "PROCESSING",
        )

        self.assertEqual(
            order.approved_by,
            self.user,
        )

        self.assertIsNotNone(
            order.approved_at,
        )

    def test_approve_invalid_status(self):

        with self.assertRaises(
            ValueError,
        ):

            SalesOrderService.approve(
                self.order,
                self.user,
            )

    # ------------------------------------
    # cancel()
    # ------------------------------------

    def test_cancel_sales_order(self):

        order = SalesOrderService.cancel(
            self.order,
        )

        self.assertEqual(
            order.status,
            "CANCELLED",
        )

    def test_cancel_completed_order(self):

        self.order.status = "COMPLETED"

        self.order.save()

        with self.assertRaises(
            ValueError,
        ):

            SalesOrderService.cancel(
                self.order,
            )

    # ------------------------------------
    # mark_processing()
    # ------------------------------------

    def test_mark_processing(self):

        self.order.status = "CONFIRMED"

        self.order.save()

        order = (
            SalesOrderService.mark_processing(
                self.order,
            )
        )

        self.assertEqual(
            order.status,
            "PROCESSING",
        )

    def test_mark_processing_invalid_status(self):

        with self.assertRaises(
            ValueError,
        ):

            SalesOrderService.mark_processing(
                self.order,
            )