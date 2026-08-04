from rest_framework import serializers

from .models import (
    User,
    UserProfile,
    Role,
)


class RoleSerializer(serializers.ModelSerializer):
    """
    Organization Role Serializer
    """

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    class Meta:

        model = Role

        fields = [
            "id",
            "organization",
            "organization_name",
            "name",
            "description",
            "permissions",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "organization_name",
            "created_at",
            "updated_at",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    """
    User Profile Serializer
    """

    class Meta:

        model = UserProfile

        fields = [
            "id",
            "date_of_birth",
            "gender",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "emergency_contact_name",
            "emergency_contact_number",
            "bio",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    role_name = serializers.CharField(
        source="role.name",
        read_only=True,
    )

    profile = UserProfileSerializer(
        read_only=True,
    )

    class Meta:

        model = User

        fields = [
            "id",

            "username",
            "first_name",
            "last_name",

            "email",
            "phone_number",

            "profile_picture",

            "organization",
            "organization_name",

            "role",
            "role_name",

            "is_active",
            "is_staff",
            "is_superuser",

            "is_verified",

            "profile",

            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "organization_name",
            "role_name",
            "created_at",
            "updated_at",
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer used while creating users.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:

        model = User

        fields = [
            "username",
            "first_name",
            "last_name",

            "email",
            "password",

            "phone_number",

            "organization",

            "role",
        ]

    def create(self, validated_data):

        password = validated_data.pop(
            "password"
        )

        user = User(
            **validated_data
        )

        user.set_password(
            password
        )

        user.save()

        return user