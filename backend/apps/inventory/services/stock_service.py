from django.db import transaction

from apps.inventory.models import Stock


class StockService:
    """
    Service responsible for all stock quantity operations.

    Every module (Purchases, Sales, Manufacturing,
    Stock Transfer, Returns) should use this service
    instead of directly modifying the Stock model.
    """

    @staticmethod
    @transaction.atomic
    def get_or_create_stock(
        *,
        product,
        warehouse,
    ):
        """
        Returns the stock record for a product in a warehouse.
        Creates it if it does not already exist.
        """

        stock, created = Stock.objects.get_or_create(
            product=product,
            warehouse=warehouse,
            defaults={
                "quantity": 0,
                "reserved_quantity": 0,
            },
        )

        return stock

    @staticmethod
    @transaction.atomic
    def increase_stock(
        *,
        product,
        warehouse,
        quantity,
    ):
        """
        Increase available stock.

        Used by:
            - Purchase Receipts
            - Sales Returns
            - Opening Stock
            - Stock Adjustments (+)
        """

        stock = StockService.get_or_create_stock(
            product=product,
            warehouse=warehouse,
        )

        stock.quantity += quantity
        stock.save()

        return stock

    @staticmethod
    @transaction.atomic
    def decrease_stock(
        *,
        product,
        warehouse,
        quantity,
    ):
        """
        Decrease stock.

        Used by:
            - Sales
            - Purchase Returns
            - Stock Adjustments (-)
            - Manufacturing Consumption
        """

        stock = StockService.get_or_create_stock(
            product=product,
            warehouse=warehouse,
        )

        if stock.available_quantity < quantity:
            raise ValueError(
                "Insufficient stock available."
            )

        stock.quantity -= quantity
        stock.save()

        return stock

    @staticmethod
    @transaction.atomic
    def reserve_stock(
        *,
        product,
        warehouse,
        quantity,
    ):
        """
        Reserve stock for Sales Orders.
        """

        stock = StockService.get_or_create_stock(
            product=product,
            warehouse=warehouse,
        )

        if stock.available_quantity < quantity:
            raise ValueError(
                "Insufficient available stock."
            )

        stock.reserved_quantity += quantity
        stock.save()

        return stock

    @staticmethod
    @transaction.atomic
    def release_reserved_stock(
        *,
        product,
        warehouse,
        quantity,
    ):
        """
        Release reserved stock.

        Used when:
            - Sales Order cancelled
            - Reservation expires
        """

        stock = StockService.get_or_create_stock(
            product=product,
            warehouse=warehouse,
        )

        if stock.reserved_quantity < quantity:
            raise ValueError(
                "Reserved quantity cannot become negative."
            )

        stock.reserved_quantity -= quantity
        stock.save()

        return stock

    @staticmethod
    def available_stock(
        *,
        product,
        warehouse,
    ):
        """
        Returns available stock quantity.
        """

        stock = StockService.get_or_create_stock(
            product=product,
            warehouse=warehouse,
        )

        return stock.available_quantity

    @staticmethod
    def inventory_value(
        *,
        product,
        warehouse,
    ):
        """
        Returns inventory value for one product.
        """

        stock = StockService.get_or_create_stock(
            product=product,
            warehouse=warehouse,
        )

        return stock.inventory_value