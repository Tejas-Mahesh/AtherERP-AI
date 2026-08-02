from django.db import models

from apps.common.models import BaseModel
from .supplier import Supplier


class SupplierContact(BaseModel):
    """
    Contact person for a supplier.
    """

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="contacts",
    )

    name = models.CharField(
        max_length=200,
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    mobile = models.CharField(
        max_length=20,
        blank=True,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Supplier Contact"
        verbose_name_plural = "Supplier Contacts"

    def __str__(self):
        return f"{self.name} ({self.supplier.name})"