from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sales.api.serializers import (
    CustomerPaymentSerializer,
)
from apps.sales.models import CustomerPayment
from apps.sales.services import CustomerPaymentService


class CustomerPaymentViewSet(ModelViewSet):
    """
    API endpoint for Customer Payments.
    """

    queryset = CustomerPayment.objects.all()

    serializer_class = CustomerPaymentSerializer

    search_fields = (
        "payment_number",
        "customer__name",
        "sales_invoice__invoice_number",
        "reference_number",
    )

    ordering_fields = (
        "payment_date",
        "amount",
        "created_at",
    )

    ordering = (
        "-payment_date",
    )

    filterset_fields = (
        "status",
        "payment_method",
        "payment_date",
        "customer",
    )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        payment = (
            CustomerPaymentService.create_payment(
                **serializer.validated_data,
            )
        )

        output = self.get_serializer(
            payment,
        )

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()