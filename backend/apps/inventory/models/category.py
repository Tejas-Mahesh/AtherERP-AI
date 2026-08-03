from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization


class Category(BaseModel):
    """
    Product Category
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "code",
                ],
                name="unique_category_code_per_organization",
            ),
        ]

    def __str__(self):
        return self.name