from django.contrib.auth.models import AbstractUser
from django.db import models
from .role import Role
from apps.common.models import BaseModel
from apps.organizations.models import Organization


class User(BaseModel, AbstractUser):
    """
    Custom User Model
    """

    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True,
    )
    role = models.ForeignKey(
    Role,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="users",
)

    is_verified = models.BooleanField(
        default=False,
    )

    failed_login_attempts = models.PositiveIntegerField(
        default=0,
    )

    account_locked_until = models.DateTimeField(
        null=True,
        blank=True,
    )

    last_password_change = models.DateTimeField(
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email
