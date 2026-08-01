from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization


class Unit(BaseModel):
    """
    Unit of Measurement (UOM)
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="units",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    symbol = models.CharField(
        max_length=10,
    )

    description = models.TextField(
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
                name="unique_unit_code_per_organization",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.symbol})"