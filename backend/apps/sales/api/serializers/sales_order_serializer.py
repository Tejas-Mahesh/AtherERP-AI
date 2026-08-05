from rest_framework import serializers

from apps.sales.models import (
    SalesOrder,
    SalesOrderItem,
)


class SalesOrderItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Sales Order Items.
    """

    class Meta:
        model = SalesOrderItem
        fields = "__all__"


class SalesOrderSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Sales Order.
    """

    items = SalesOrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = SalesOrder
        fields = "__all__"