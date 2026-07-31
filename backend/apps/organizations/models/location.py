from django.db import models

from apps.common.models import BaseModel
from .branch import Branch


class Location(BaseModel):
    """
    Represents a physical business location.
    """

    LOCATION_TYPES = [
        ("HEAD_OFFICE", "Head Office"),
        ("BRANCH_OFFICE", "Branch Office"),
        ("WAREHOUSE", "Warehouse"),
        ("STORE", "Retail Store"),
        ("FACTORY", "Factory"),
        ("SERVICE_CENTER", "Service Center"),
    ]

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="locations",
    )

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=20,
    )

    location_type = models.CharField(
        max_length=30,
        choices=LOCATION_TYPES,
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
        default="India",
    )

    postal_code = models.CharField(
        max_length=10,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    class Meta:

        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["branch", "code"],
                name="unique_location_code_per_branch",
            )
        ]

    def __str__(self):
        return f"{self.branch.name} - {self.name}"