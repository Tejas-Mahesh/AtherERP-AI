from django.db import models

from apps.common.models import BaseModel
from .warehouse import Warehouse


class WarehouseLocation(BaseModel):
    """
    Warehouse Storage Location
    """

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="locations",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=30,
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
                    "warehouse",
                    "code",
                ],
                name="unique_location_code_per_warehouse",
            ),
        ]

    def __str__(self):
        return f"{self.warehouse.code} - {self.code}"