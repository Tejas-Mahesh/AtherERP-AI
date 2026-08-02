from rest_framework import viewsets

from .models import (
    PurchaseOrder,
    PurchaseOrderItem,
    GoodsReceipt,
)

from .serializers import (
    PurchaseOrderSerializer,
    PurchaseOrderItemSerializer,
    GoodsReceiptSerializer,
)


class PurchaseOrderViewSet(viewsets.ModelViewSet):

    queryset = PurchaseOrder.objects.select_related(
        "organization",
        "supplier",
        "approved_by",
    ).prefetch_related(
        "items",
    )

    serializer_class = PurchaseOrderSerializer


class PurchaseOrderItemViewSet(viewsets.ModelViewSet):

    queryset = PurchaseOrderItem.objects.select_related(
        "purchase_order",
        "product",
    )

    serializer_class = PurchaseOrderItemSerializer


class GoodsReceiptViewSet(viewsets.ModelViewSet):

    queryset = GoodsReceipt.objects.select_related(
        "purchase_order",
        "warehouse",
        "received_by",
    )

    serializer_class = GoodsReceiptSerializer