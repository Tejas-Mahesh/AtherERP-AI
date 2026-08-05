from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sales.api.serializers import (
    SalesInvoiceSerializer,
)
from apps.sales.models import SalesInvoice
from apps.sales.services import SalesInvoiceService


class SalesInvoiceViewSet(ModelViewSet):
    """
    API endpoint for Sales Invoices.
    """

    queryset = SalesInvoice.objects.all()

    serializer_class = SalesInvoiceSerializer

    search_fields = (
        "invoice_number",
        "customer__name",
        "sales_order__sales_order_number",
    )

    ordering_fields = (
        "invoice_date",
        "total_amount",
        "created_at",
    )

    ordering = (
        "-invoice_date",
    )

    filterset_fields = (
        "status",
        "customer",
        "invoice_date",
    )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        sales_invoice = (
            SalesInvoiceService.create_sales_invoice(
                **serializer.validated_data,
            )
        )

        output = self.get_serializer(
            sales_invoice,
        )

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()