from rest_framework.viewsets import ModelViewSet

from apps.sales.models import Customer
from apps.sales.api.serializers import (
    CustomerSerializer,
)


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

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