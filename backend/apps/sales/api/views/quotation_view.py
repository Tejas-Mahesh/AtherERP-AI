from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sales.api.serializers import (
    QuotationSerializer,
)
from apps.sales.models import Quotation
from apps.sales.services import QuotationService


class QuotationViewSet(ModelViewSet):
    """
    API endpoint for Quotations.
    """

    queryset = Quotation.objects.all()

    serializer_class = QuotationSerializer

    search_fields = (
        "quotation_number",
        "customer__name",
    )

    ordering_fields = (
        "quotation_date",
        "valid_until",
        "total_amount",
    )

    ordering = (
        "-quotation_date",
    )

    filterset_fields = (
        "status",
        "quotation_date",
        "customer",
    )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True,
        )

        quotation = QuotationService.create_quotation(
            **serializer.validated_data,
        )

        output = self.get_serializer(
            quotation,
        )

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )