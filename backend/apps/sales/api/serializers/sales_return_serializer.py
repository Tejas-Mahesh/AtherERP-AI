from rest_framework import serializers

from apps.sales.models import (
    SalesReturn,
    SalesReturnItem,
)


class SalesReturnItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Sales Return Item.
    """

    class Meta:
        model = SalesReturnItem
        fields = "__all__"


class SalesReturnSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Sales Return.
    """

    items = SalesReturnItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = SalesReturn
        fields = "__all__"