from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization


class Supplier(BaseModel):
    """
    Represents a supplier/vendor for an organization.
    """

    STATUS_CHOICES = (
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("BLOCKED", "Blocked"),
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="suppliers",
    )

    supplier_code = models.CharField(
        max_length=20,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    company_name = models.CharField(
        max_length=200,
        blank=True,
    )

    contact_person = models.CharField(
        max_length=200,
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

    website = models.URLField(
        blank=True,
    )

    gst_number = models.CharField(
        max_length=20,
        blank=True,
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True,
    )

    payment_terms = models.CharField(
        max_length=100,
        blank=True,
    )

    credit_limit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return f"{self.supplier_code} - {self.name}"