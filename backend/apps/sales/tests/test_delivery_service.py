from unittest.mock import patch

from django.test import TestCase

from apps.inventory.models import Stock
from apps.sales.services import DeliveryService


class DeliveryServiceTest(TestCase):
    """
    Tests for DeliveryService.
    """

    @patch(
        "apps.sales.services.delivery_service.SalesOrderStatusService.update_status"
    )
    @patch(
        "apps.sales.services.delivery_service.StockTransactionService.sale"
    )
    def test_deliver_items_success(
        self,
        mock_sale,
        mock_update_status,
    ):

        stock = Stock()

        stock.quantity = 20

        stock.available_quantity = 20

        stock.save = lambda: None

        product = type(
            "Product",
            (),
            {
                "name": "Laptop",
            },
        )()

        sales_order_item = type(
            "SalesOrderItem",
            (),
            {
                "product": product,
                "delivered_quantity": 0,
                "save": lambda self: None,
            },
        )()

        warehouse = object()

        delivery_note = type(
            "DeliveryNote",
            (),
            {
                "warehouse": warehouse,
                "delivery_number": "DN0001",
                "sales_order": object(),
            },
        )()

        with patch(
            "apps.sales.services.delivery_service.Stock.objects.select_for_update"
        ) as mock_stock:

            mock_stock.return_value.get.return_value = stock

            DeliveryService.deliver_items(
                delivery_note,
                [
                    {
                        "sales_order_item": sales_order_item,
                        "quantity": 5,
                        "location": None,
                    }
                ],
            )

            self.assertEqual(
                stock.quantity,
                15,
            )

            self.assertEqual(
                sales_order_item.delivered_quantity,
                5,
            )

            mock_sale.assert_called_once()

            mock_update_status.assert_called_once()

    def test_insufficient_stock(self):

        stock = Stock()

        stock.quantity = 2

        stock.available_quantity = 2

        product = type(
            "Product",
            (),
            {
                "name": "Laptop",
            },
        )()

        sales_order_item = type(
            "SalesOrderItem",
            (),
            {
                "product": product,
                "delivered_quantity": 0,
            },
        )()

        warehouse = object()

        delivery_note = type(
            "DeliveryNote",
            (),
            {
                "warehouse": warehouse,
                "delivery_number": "DN0001",
                "sales_order": object(),
            },
        )()

        with patch(
            "apps.sales.services.delivery_service.Stock.objects.select_for_update"
        ) as mock_stock:

            mock_stock.return_value.get.return_value = stock

            with self.assertRaises(
                ValueError,
            ):

                DeliveryService.deliver_items(
                    delivery_note,
                    [
                        {
                            "sales_order_item": sales_order_item,
                            "quantity": 5,
                            "location": None,
                        }
                    ],
                )