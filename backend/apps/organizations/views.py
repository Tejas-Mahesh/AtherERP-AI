from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    Organization,
    Branch,
    Location,
)

from .serializers import (
    OrganizationSerializer,
    BranchSerializer,
    LocationSerializer,
)

from .filters import (
    OrganizationFilter,
    BranchFilter,
    LocationFilter,
)

from .permissions import (
    IsAdminOrReadOnly,
)


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    Organization API
    """

    queryset = Organization.objects.all()

    serializer_class = OrganizationSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = OrganizationFilter

    search_fields = [
        "name",
        "legal_name",
        "email",
        "phone",
        "city",
        "state",
        "country",
    ]

    ordering_fields = [
        "name",
        "created_at",
        "updated_at",
    ]

    ordering = [
        "name",
    ]


class BranchViewSet(viewsets.ModelViewSet):
    """
    Branch API
    """

    queryset = Branch.objects.select_related(
        "organization",
    )

    serializer_class = BranchSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = BranchFilter

    search_fields = [
        "name",
        "code",
        "city",
        "state",
        "email",
    ]

    ordering_fields = [
        "name",
        "code",
        "created_at",
    ]

    ordering = [
        "name",
    ]


class LocationViewSet(viewsets.ModelViewSet):
    """
    Location API
    """

    queryset = Location.objects.select_related(
        "branch",
        "branch__organization",
    )

    serializer_class = LocationSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = LocationFilter

    search_fields = [
        "name",
        "code",
        "city",
        "state",
        "location_type",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = [
        "name",
    ]