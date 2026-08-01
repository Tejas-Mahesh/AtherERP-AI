from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization
from apps.accounts.models import User


class Warehouse(BaseModel):
    """
    Warehouse Master
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="warehouses",
    )

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=20,
    )

    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_warehouses",
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
    )

    postal_code = models.CharField(
        max_length=20,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:

        ordering = [
            "name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "code",
                ],
                name="unique_warehouse_code_per_organization",
            ),
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"