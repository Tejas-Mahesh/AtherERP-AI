from rest_framework import serializers

from .models import User, UserProfile, Role


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=False,
    )

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "last_login",
        )