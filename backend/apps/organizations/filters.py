import django_filters

from .models import (
    Organization,
    Branch,
    Location,
)


class OrganizationFilter(django_filters.FilterSet):
    """
    Organization Filters
    """

    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    legal_name = django_filters.CharFilter(
        field_name="legal_name",
        lookup_expr="icontains",
    )

    city = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    state = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    country = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    class Meta:
        model = Organization

        fields = [
            "name",
            "legal_name",
            "city",
            "state",
            "country",
        ]


class BranchFilter(django_filters.FilterSet):
    """
    Branch Filters
    """

    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    code = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    city = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    state = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    organization = django_filters.UUIDFilter(
        field_name="organization__id",
    )

    is_head_office = django_filters.BooleanFilter()

    class Meta:
        model = Branch

        fields = [
            "organization",
            "name",
            "code",
            "city",
            "state",
            "is_head_office",
        ]


class LocationFilter(django_filters.FilterSet):
    """
    Location Filters
    """

    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    code = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    city = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    state = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    branch = django_filters.UUIDFilter(
        field_name="branch__id",
    )

    location_type = django_filters.CharFilter()

    class Meta:
        model = Location

        fields = [
            "branch",
            "name",
            "code",
            "city",
            "state",
            "location_type",
        ]