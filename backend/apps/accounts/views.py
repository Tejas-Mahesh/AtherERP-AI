from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    User,
    Role,
    UserProfile,
)

from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    RoleSerializer,
    UserProfileSerializer,
)

from .filters import (
    UserFilter,
    RoleFilter,
)

from .permissions import (
    IsAdminOrReadOnly,
)

from .services import (
    UserService,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    User API
    """

    queryset = User.objects.select_related(
        "organization",
        "role",
    ).prefetch_related(
        "profile",
    )

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = UserFilter

    search_fields = [
        "first_name",
        "last_name",
        "username",
        "email",
        "phone_number",
    ]

    ordering_fields = [
        "first_name",
        "last_name",
        "email",
        "created_at",
    ]

    ordering = [
        "first_name",
    ]

    def get_serializer_class(self):

        if self.action == "create":
            return UserCreateSerializer

        return UserSerializer

    def perform_create(self, serializer):

        UserService.create_user(
            **serializer.validated_data
        )

    @action(
        detail=True,
        methods=["post"],
    )
    def activate(self, request, pk=None):

        user = self.get_object()

        UserService.activate_user(user)

        return Response(
            {
                "message": "User activated successfully."
            }
        )

    @action(
        detail=True,
        methods=["post"],
    )
    def deactivate(self, request, pk=None):

        user = self.get_object()

        UserService.deactivate_user(user)

        return Response(
            {
                "message": "User deactivated successfully."
            }
        )

    @action(
        detail=True,
        methods=["post"],
    )
    def verify(self, request, pk=None):

        user = self.get_object()

        UserService.verify_user(user)

        return Response(
            {
                "message": "User verified successfully."
            }
        )


class RoleViewSet(viewsets.ModelViewSet):
    """
    Role API
    """

    queryset = Role.objects.select_related(
        "organization",
    ).prefetch_related(
        "permissions",
    )

    serializer_class = RoleSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = RoleFilter

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = [
        "name",
    ]


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    User Profile API
    """

    queryset = UserProfile.objects.select_related(
        "user",
    )

    serializer_class = UserProfileSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "user__first_name",
        "user__last_name",
        "city",
        "state",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]