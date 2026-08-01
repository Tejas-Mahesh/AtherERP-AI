from .models import (
    Product,
    Stock,
    Warehouse,
)


class ProductSelector:

    @staticmethod
    def get_all():

        return Product.objects.select_related(
            "organization",
            "category",
            "brand",
            "unit",
        )

    @staticmethod
    def get_by_id(pk):

        return Product.objects.select_related(
            "organization",
            "category",
            "brand",
            "unit",
        ).get(pk=pk)


class WarehouseSelector:

    @staticmethod
    def get_all():

        return Warehouse.objects.select_related(
            "organization",
            "manager",
        )

    @staticmethod
    def get_by_id(pk):

        return Warehouse.objects.select_related(
            "organization",
            "manager",
        ).get(pk=pk)


class StockSelector:

    @staticmethod
    def get_all():

        return Stock.objects.select_related(
            "product",
            "warehouse",
            "product__category",
            "product__brand",
            "product__unit",
        )

    @staticmethod
    def get_by_id(pk):

        return Stock.objects.select_related(
            "product",
            "warehouse",
            "product__category",
            "product__brand",
            "product__unit",
        ).get(pk=pk)

    @staticmethod
    def low_stock():

        queryset = Stock.objects.select_related(
            "product",
            "warehouse",
        )

        return [
            stock
            for stock in queryset
            if stock.quantity <= stock.product.reorder_level
        ]