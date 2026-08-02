from rest_framework import serializers

from .models import (
    PurchaseOrder,
    PurchaseOrderItem,
    GoodsReceipt,
)


class PurchaseOrderItemSerializer(serializers.ModelSerializer):

    remaining_quantity = serializers.ReadOnlyField()

    class Meta:
        model = PurchaseOrderItem
        fields = "__all__"


class PurchaseOrderSerializer(serializers.ModelSerializer):

    items = PurchaseOrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class GoodsReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsReceipt
        fields = "__all__"