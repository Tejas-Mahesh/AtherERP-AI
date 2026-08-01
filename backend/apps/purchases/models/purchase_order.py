
from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization
# from apps.suppliers.models import Supplier
from apps.accounts.models import User


class PurchaseOrder(BaseModel):
    """
    Purchase Order
    """

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("SUBMITTED", "Submitted"),
        ("APPROVED", "Approved"),
        ("ORDERED", "Ordered"),
        ("PARTIALLY_RECEIVED", "Partially Received"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="purchase_orders",
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="purchase_orders",
    )

    purchase_number = models.CharField(
        max_length=30,
        unique=True,
    )

    order_date = models.DateField()

    expected_delivery_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    tax_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    discount_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    remarks = models.TextField(
        blank=True,
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_purchase_orders",
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:

        ordering = [
            "-order_date",
        ]

    def __str__(self):
        return self.purchase_number