from rest_framework import serializers

from apps.sales.models import (
    DeliveryNote,
    DeliveryNoteItem,
)


class DeliveryNoteItemSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Delivery Note Items.
    """

    class Meta:
        model = DeliveryNoteItem
        fields = "__all__"


class DeliveryNoteSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for Delivery Note.
    """

    items = DeliveryNoteItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = DeliveryNote
        fields = "__all__"