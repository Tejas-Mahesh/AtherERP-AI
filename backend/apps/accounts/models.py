from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    """
    Custom user model for AetherERP AI.
    """

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email