from django.db import models
from django.contrib.auth.models import Permission

from apps.common.models import BaseModel
from apps.organizations.models import Organization


class Role(BaseModel):
    """
    Organization-specific role.
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="roles",
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    permissions = models.ManyToManyField(
        Permission,
        blank=True,
    )

    class Meta:

        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["organization", "name"],
                name="unique_role_per_organization",
            )
        ]

    def __str__(self):
        return f"{self.organization.name} - {self.name}"