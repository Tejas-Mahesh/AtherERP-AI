from unittest.mock import patch

from django.test import TestCase

from apps.accounts.models import User
from apps.sales.models import (
    Customer,
    SalesReturn,
)
from apps.sales.services import (
    SalesReturnService,
)


class SalesReturnServiceTest(TestCase):
    """
    Tests for SalesReturnService.
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

        self.sales_return = SalesReturn.objects.create(
            return_number="SR0001",
            customer=self.customer,
            status="DRAFT",
        )

    # ------------------------------------
    # receive_return()
    # ------------------------------------

    @patch(
        "apps.sales.services.sales_return_service.StockTransactionService.sales_return"
    )
    @patch(
        "apps.sales.services.sales_return_service.StockService.increase_stock"
    )
    def test_receive_return(
        self,
        mock_increase_stock,
        mock_sales_return,
    ):

        location = type(
            "Location",
            (),
            {
                "warehouse": object(),
            },
        )()

        product = object()

        item = type(
            "ReturnItem",
            (),
            {
                "location": location,
                "product": product,
                "quantity": 5,
            },
        )()

        self.sales_return.items = type(
            "Manager",
            (),
            {
                "all": lambda self: [item],
            },
        )()

        sales_return = (
            SalesReturnService.receive_return(
                self.sales_return,
                received_by=self.user,
            )
        )

        self.assertEqual(
            sales_return.status,
            "RECEIVED",
        )

        mock_increase_stock.assert_called_once()

        mock_sales_return.assert_called_once()

    def test_receive_return_invalid_status(self):

        self.sales_return.status = "APPROVED"

        self.sales_return.save()

        with self.assertRaises(
            ValueError,
        ):

            SalesReturnService.receive_return(
                self.sales_return,
            )

    # ------------------------------------
    # approve()
    # ------------------------------------

    def test_approve_return(self):

        self.sales_return.status = "RECEIVED"

        self.sales_return.save()

        sales_return = (
            SalesReturnService.approve(
                self.sales_return,
                self.user,
            )
        )

        self.assertEqual(
            sales_return.status,
            "APPROVED",
        )

        self.assertEqual(
            sales_return.approved_by,
            self.user,
        )

    def test_approve_invalid_status(self):

        with self.assertRaises(
            ValueError,
        ):

            SalesReturnService.approve(
                self.sales_return,
                self.user,
            )

    # ------------------------------------
    # refund()
    # ------------------------------------

    @patch(
        "apps.sales.services.sales_return_service.SalesReturnService.calculate_total"
    )
    def test_refund(
        self,
        mock_calculate_total,
    ):

        self.sales_return.status = "APPROVED"

        self.sales_return.save()

        sales_return = (
            SalesReturnService.refund(
                self.sales_return,
            )
        )

        self.assertEqual(
            sales_return.status,
            "REFUNDED",
        )

        mock_calculate_total.assert_called_once_with(
            self.sales_return,
        )

    def test_refund_invalid_status(self):

        with self.assertRaises(
            ValueError,
        ):

            SalesReturnService.refund(
                self.sales_return,
            )

    # ------------------------------------
    # reject()
    # ------------------------------------

    def test_reject_return(self):

        sales_return = (
            SalesReturnService.reject(
                self.sales_return,
            )
        )

        self.assertEqual(
            sales_return.status,
            "REJECTED",
        )

    def test_reject_refunded_return(self):

        self.sales_return.status = "REFUNDED"

        self.sales_return.save()

        with self.assertRaises(
            ValueError,
        ):

            SalesReturnService.reject(
                self.sales_return,
            )