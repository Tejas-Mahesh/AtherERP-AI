import django_filters

from .models import (
    User,
    Role,
)


class UserFilter(django_filters.FilterSet):
    """
    User Filters
    """

    organization = django_filters.UUIDFilter(
        field_name="organization__id",
    )

    role = django_filters.UUIDFilter(
        field_name="role__id",
    )

    first_name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    last_name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    username = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    email = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    phone_number = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    is_active = django_filters.BooleanFilter()

    is_verified = django_filters.BooleanFilter()

    is_staff = django_filters.BooleanFilter()

    is_superuser = django_filters.BooleanFilter()

    class Meta:

        model = User

        fields = [
            "organization",
            "role",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "is_active",
            "is_verified",
            "is_staff",
            "is_superuser",
        ]


class RoleFilter(django_filters.FilterSet):
    """
    Role Filters
    """

    organization = django_filters.UUIDFilter(
        field_name="organization__id",
    )

    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    class Meta:

        model = Role

        fields = [
            "organization",
            "name",
        ]