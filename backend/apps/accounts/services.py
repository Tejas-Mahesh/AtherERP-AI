from django.db import transaction

from .models import User, UserProfile, Role


class UserService:
    """
    Business logic for User operations.
    """

    @staticmethod
    @transaction.atomic
    def create_user(**validated_data):
        password = validated_data.pop("password", None)

        user = User(**validated_data)

        if password:
            user.set_password(password)

        user.save()

        return user

    @staticmethod
    @transaction.atomic
    def update_user(instance, **validated_data):

        password = validated_data.pop("password", None)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance

    @staticmethod
    @transaction.atomic
    def deactivate_user(instance):

        instance.is_active = False
        instance.save()

        return instance

    @staticmethod
    @transaction.atomic
    def activate_user(instance):

        instance.is_active = True
        instance.save()

        return instance


class UserProfileService:

    @staticmethod
    @transaction.atomic
    def update_profile(instance, **validated_data):

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance


class RoleService:

    @staticmethod
    @transaction.atomic
    def create_role(**validated_data):
        return Role.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_role(instance, **validated_data):

        permissions = validated_data.pop("permissions", None)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        if permissions is not None:
            instance.permissions.set(permissions)

        return instance