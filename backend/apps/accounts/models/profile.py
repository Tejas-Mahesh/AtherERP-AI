from django.db import models

from apps.common.models import BaseModel

from .user import User


class UserProfile(BaseModel):
    """
    Additional information about a user.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=10,
        blank=True,
    )

    emergency_contact_name = models.CharField(
        max_length=100,
        blank=True,
    )

    emergency_contact_number = models.CharField(
        max_length=20,
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    def __str__(self):
        return f"{self.user.email} Profile"