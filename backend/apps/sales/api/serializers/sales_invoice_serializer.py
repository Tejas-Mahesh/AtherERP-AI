from rest_framework import serializers

from apps.sales.models import (
    SalesInvoice,
    SalesInvoiceItem,
)


class SalesInvoiceItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Sales Invoice Items.
    """

    class Meta:
        model = SalesInvoiceItem
        fields = "__all__"


class SalesInvoiceSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Sales Invoice.
    """

    items = SalesInvoiceItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = SalesInvoice
        fields = "__all__"