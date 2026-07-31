from rest_framework import viewsets

from .models import User, UserProfile, Role

from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    RoleSerializer,
)

from .selectors import (
    UserSelector,
    UserProfileSelector,
    RoleSelector,
)

from .services import (
    UserService,
    UserProfileService,
    RoleService,
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = UserSelector.get_all()

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        UserService.create_user(
            **serializer.validated_data
        )

    def perform_update(self, serializer):
        UserService.update_user(
            self.get_object(),
            **serializer.validated_data
        )


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfileSelector.get_all()

    serializer_class = UserProfileSerializer

    def perform_update(self, serializer):
        UserProfileService.update_profile(
            self.get_object(),
            **serializer.validated_data
        )


class RoleViewSet(viewsets.ModelViewSet):

    queryset = RoleSelector.get_all()

    serializer_class = RoleSerializer

    def perform_create(self, serializer):
        RoleService.create_role(
            **serializer.validated_data
        )

    def perform_update(self, serializer):
        RoleService.update_role(
            self.get_object(),
            **serializer.validated_data
        )