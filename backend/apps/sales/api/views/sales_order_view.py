from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sales.api.serializers import (
    SalesOrderSerializer,
)
from apps.sales.models import SalesOrder
from apps.sales.services import SalesOrderService


class SalesOrderViewSet(ModelViewSet):
    """
    API endpoint for Sales Orders.
    """

    queryset = SalesOrder.objects.all()

    serializer_class = SalesOrderSerializer

    search_fields = (
        "sales_order_number",
        "customer__name",
    )

    ordering_fields = (
        "order_date",
        "expected_delivery_date",
        "total_amount",
    )

    ordering = (
        "-order_date",
    )

    filterset_fields = (
        "status",
        "customer",
        "order_date",
    )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        sales_order = SalesOrderService.create_sales_order(
            **serializer.validated_data,
        )

        output = self.get_serializer(
            sales_order,
        )

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()