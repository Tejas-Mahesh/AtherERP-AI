from django.db import transaction

from apps.inventory.models import (
    Stock,
    StockTransaction,
)
from apps.inventory.services.stock_transaction_service import (
    StockTransactionService,
)

from apps.sales.services.sales_order_status_service import (
    SalesOrderStatusService,
)


class DeliveryService:
    """
    Process product deliveries.
    """

    @staticmethod
    @transaction.atomic
    def deliver_items(
        delivery_note,
        items,
    ):
        """
        items = [
            {
                "sales_order_item": SalesOrderItem,
                "quantity": 5,
                "location": WarehouseLocation | None,
            }
        ]
        """

        for entry in items:

            sales_order_item = entry["sales_order_item"]
            delivered_qty = entry["quantity"]
            location = entry.get("location")

            stock = Stock.objects.select_for_update().get(
                warehouse=delivery_note.warehouse,
                product=sales_order_item.product,
            )

            if stock.available_quantity < delivered_qty:
                raise ValueError(
                    f"Insufficient stock for "
                    f"{sales_order_item.product.name}"
                )

            stock.quantity -= delivered_qty
            stock.save()

            StockTransactionService.sale(
    product=sales_order_item.product,
    warehouse=delivery_note.warehouse,
    quantity=delivered_qty,
    reference_number=delivery_note.delivery_number,
    location=location,
)

            sales_order_item.delivered_quantity += delivered_qty
            sales_order_item.save()

        SalesOrderStatusService.update_status(
            delivery_note.sales_order
        )

        return delivery_note