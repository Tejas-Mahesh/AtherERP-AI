from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization


class Brand(BaseModel):
    """
    Product Brand
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="brands",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
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
                name="unique_brand_code_per_organization",
            ),
        ]

    def __str__(self):
        return self.name