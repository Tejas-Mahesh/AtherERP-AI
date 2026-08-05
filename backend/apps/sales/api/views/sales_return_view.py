from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sales.api.serializers import (
    SalesReturnSerializer,
)
from apps.sales.models import SalesReturn
from apps.sales.services import SalesReturnService


class SalesReturnViewSet(ModelViewSet):
    """
    API endpoint for Sales Returns.
    """

    queryset = SalesReturn.objects.all()

    serializer_class = SalesReturnSerializer

    search_fields = (
        "return_number",
        "customer__name",
        "sales_invoice__invoice_number",
    )

    ordering_fields = (
        "return_date",
        "total_amount",
        "created_at",
    )

    ordering = (
        "-return_date",
    )

    filterset_fields = (
        "status",
        "customer",
        "return_date",
    )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        sales_return = (
            SalesReturnService.create_sales_return(
                **serializer.validated_data,
            )
        )

        output = self.get_serializer(
            sales_return,
        )

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()