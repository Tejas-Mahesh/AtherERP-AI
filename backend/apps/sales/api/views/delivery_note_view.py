from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sales.api.serializers import (
    DeliveryNoteSerializer,
)
from apps.sales.models import DeliveryNote
from apps.sales.services import DeliveryService


class DeliveryNoteViewSet(ModelViewSet):
    """
    API endpoint for Delivery Notes.
    """

    queryset = DeliveryNote.objects.all()

    serializer_class = DeliveryNoteSerializer

    search_fields = (
        "delivery_number",
        "sales_order__sales_order_number",
        "sales_order__customer__name",
    )

    ordering_fields = (
        "delivery_date",
        "created_at",
    )

    ordering = (
        "-delivery_date",
    )

    filterset_fields = (
        "status",
        "warehouse",
        "delivery_date",
    )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        delivery_note = DeliveryService.create_delivery_note(
            **serializer.validated_data,
        )

        output = self.get_serializer(
            delivery_note,
        )

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()