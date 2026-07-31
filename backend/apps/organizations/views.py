from rest_framework import viewsets

from .serializers import (
    OrganizationSerializer,
    BranchSerializer,
    LocationSerializer,
)

from .selectors import (
    OrganizationSelector,
    BranchSelector,
    LocationSelector,
)

from .services import (
    OrganizationService,
    BranchService,
    LocationService,
)


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = OrganizationSelector.get_all()

    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        OrganizationService.create_organization(
            **serializer.validated_data
        )

    def perform_update(self, serializer):
        OrganizationService.update_organization(
            self.get_object(),
            **serializer.validated_data
        )


class BranchViewSet(viewsets.ModelViewSet):

    queryset = BranchSelector.get_all()

    serializer_class = BranchSerializer

    def perform_create(self, serializer):
        BranchService.create_branch(
            **serializer.validated_data
        )

    def perform_update(self, serializer):
        BranchService.update_branch(
            self.get_object(),
            **serializer.validated_data
        )


class LocationViewSet(viewsets.ModelViewSet):

    queryset = LocationSelector.get_all()

    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        LocationService.create_location(
            **serializer.validated_data
        )

    def perform_update(self, serializer):
        LocationService.update_location(
            self.get_object(),
            **serializer.validated_data
        )