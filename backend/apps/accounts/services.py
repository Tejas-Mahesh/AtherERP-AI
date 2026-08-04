from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

from .models import (
    User,
    UserProfile,
    Role,
)


class UserService:
    """
    Business logic for User management.
    """

    @staticmethod
    @transaction.atomic
    def create_user(**validated_data):
        """
        Create a new user with encrypted password
        and an empty profile.
        """

        password = validated_data.pop("password")

        validate_password(password)

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        UserProfile.objects.create(
            user=user,
        )

        return user

    @staticmethod
    @transaction.atomic
    def change_password(
        user,
        new_password,
    ):
        """
        Change user password.
        """

        validate_password(new_password)

        user.set_password(new_password)

        user.last_password_change = timezone.now()

        user.save()

        return user

    @staticmethod
    @transaction.atomic
    def verify_user(user):
        """
        Verify user account.
        """

        user.is_verified = True

        user.save(
            update_fields=[
                "is_verified",
            ]
        )

        return user

    @staticmethod
    @transaction.atomic
    def activate_user(user):

        user.is_active = True

        user.save(
            update_fields=[
                "is_active",
            ]
        )

        return user

    @staticmethod
    @transaction.atomic
    def deactivate_user(user):

        user.is_active = False

        user.save(
            update_fields=[
                "is_active",
            ]
        )

        return user

    @staticmethod
    @transaction.atomic
    def lock_account(
        user,
        minutes=30,
    ):
        """
        Lock account for failed login attempts.
        """

        user.account_locked_until = (
            timezone.now()
            + timezone.timedelta(minutes=minutes)
        )

        user.save(
            update_fields=[
                "account_locked_until",
            ]
        )

        return user

    @staticmethod
    @transaction.atomic
    def unlock_account(user):

        user.failed_login_attempts = 0

        user.account_locked_until = None

        user.save(
            update_fields=[
                "failed_login_attempts",
                "account_locked_until",
            ]
        )

        return user

    @staticmethod
    @transaction.atomic
    def assign_role(
        user,
        role,
    ):
        """
        Assign organization role.
        """

        if not isinstance(role, Role):
            raise ValidationError(
                "Invalid role."
            )

        user.role = role

        user.save(
            update_fields=[
                "role",
            ]
        )

        return user

    @staticmethod
    @transaction.atomic
    def move_to_organization(
        user,
        organization,
    ):
        """
        Transfer user to another organization.
        """

        user.organization = organization

        user.save(
            update_fields=[
                "organization",
            ]
        )

        return user