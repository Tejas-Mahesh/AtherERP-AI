from .models import (
    PurchaseOrder,
    GoodsReceipt,
)


class PurchaseOrderSelector:

    @staticmethod
    def get_all():

        return PurchaseOrder.objects.select_related(
            "organization",
            "supplier",
            "approved_by",
        )

    @staticmethod
    def get_by_id(pk):

        return PurchaseOrder.objects.select_related(
            "organization",
            "supplier",
            "approved_by",
        ).prefetch_related(
            "items",
        ).get(pk=pk)

    @staticmethod
    def by_status(status):

        return PurchaseOrder.objects.filter(
            status=status
        ).select_related(
            "organization",
            "supplier",
        )


class GoodsReceiptSelector:

    @staticmethod
    def get_all():

        return GoodsReceipt.objects.select_related(
            "purchase_order",
            "warehouse",
            "received_by",
        )

    @staticmethod
    def get_by_id(pk):

        return GoodsReceipt.objects.select_related(
            "purchase_order",
            "warehouse",
            "received_by",
        ).get(pk=pk)