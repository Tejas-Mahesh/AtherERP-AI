from django.db import models

from apps.common.models import BaseModel
from .supplier import Supplier


class SupplierDocument(BaseModel):
    """
    Documents uploaded for a supplier.
    """

    DOCUMENT_TYPES = (
        ("GST", "GST Certificate"),
        ("PAN", "PAN Card"),
        ("MSME", "MSME Certificate"),
        ("AGREEMENT", "Vendor Agreement"),
        ("BANK", "Cancelled Cheque"),
        ("ISO", "ISO Certificate"),
        ("OTHER", "Other"),
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    document_type = models.CharField(
        max_length=30,
        choices=DOCUMENT_TYPES,
    )

    document_name = models.CharField(
        max_length=200,
    )

    document = models.FileField(
        upload_to="suppliers/documents/",
    )

    description = models.TextField(
        blank=True,
    )

    expiry_date = models.DateField(
        null=True,
        blank=True,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["document_name"]
        verbose_name = "Supplier Document"
        verbose_name_plural = "Supplier Documents"

    def __str__(self):
        return f"{self.supplier.name} - {self.document_name}"