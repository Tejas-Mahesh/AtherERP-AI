from rest_framework import serializers

from apps.sales.models import (
    Quotation,
    QuotationItem,
)


class QuotationItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Quotation Items.
    """

    class Meta:
        model = QuotationItem
        fields = "__all__"


class QuotationSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Quotation.
    """

    items = QuotationItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Quotation
        fields = "__all__"