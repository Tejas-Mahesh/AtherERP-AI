from django.db import models

from apps.common.models import BaseModel
from .organizations import Organization


class Branch(BaseModel):
    """
    Represents a branch of an organization.
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="branches",
    )

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=20,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
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

    is_head_office = models.BooleanField(
        default=False,
    )

    class Meta:

        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="unique_branch_code_per_organization",
            )
        ]

    def __str__(self):
        return f"{self.organization.name} - {self.name}"