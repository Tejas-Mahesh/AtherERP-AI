from django.db import models

from apps.common.models import BaseModel


class Organization(BaseModel):
    """
    Represents a company using AetherERP AI.
    """

    name = models.CharField(
        max_length=255,
        unique=True
    )

    legal_name = models.CharField(
        max_length=255,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    tax_number = models.CharField(
        max_length=100,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        default="India"
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True
    )

    logo = models.ImageField(
        upload_to="organization_logos/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name