from rest_framework.viewsets import ModelViewSet

from apps.sales.models import Customer
from apps.sales.api.serializers import (
    CustomerSerializer,
)


class CustomerViewSet(ModelViewSet):
    """
    API endpoint for Customers.
    """

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

    search_fields = (
        "customer_code",
        "name",
        "email",
        "phone_number",
    )

    ordering_fields = (
        "customer_code",
        "name",
        "created_at",
    )

    ordering = (
        "customer_code",
    )

    filterset_fields = (
        "customer_type",
        "is_active",
    )