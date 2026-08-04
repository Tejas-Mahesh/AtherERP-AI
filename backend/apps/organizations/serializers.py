from rest_framework import serializers

from .models import (
    Organization,
    Branch,
    Location,
)


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Organization Serializer
    """

    class Meta:
        model = Organization

        fields = [
            "id",
            "name",
            "legal_name",
            "email",
            "phone",
            "website",
            "tax_number",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "logo",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class BranchSerializer(serializers.ModelSerializer):
    """
    Branch Serializer
    """

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    class Meta:
        model = Branch

        fields = [
            "id",
            "organization",
            "organization_name",
            "name",
            "code",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "is_head_office",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "organization_name",
            "created_at",
            "updated_at",
        ]


class LocationSerializer(serializers.ModelSerializer):
    """
    Location Serializer
    """

    branch_name = serializers.CharField(
        source="branch.name",
        read_only=True,
    )

    organization_name = serializers.CharField(
        source="branch.organization.name",
        read_only=True,
    )

    class Meta:
        model = Location

        fields = [
            "id",
            "branch",
            "branch_name",
            "organization_name",
            "name",
            "code",
            "location_type",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "phone",
            "email",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "branch_name",
            "organization_name",
            "created_at",
            "updated_at",
        ]