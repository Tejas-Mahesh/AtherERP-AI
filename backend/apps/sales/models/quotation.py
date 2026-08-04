from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization
from apps.accounts.models import User

from .customer import Customer


class Quotation(BaseModel):
    """
    Sales Quotation
    """

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("SENT", "Sent"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("EXPIRED", "Expired"),
        ("CONVERTED", "Converted"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="quotations",
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="quotations",
    )

    quotation_number = models.CharField(
        max_length=30,
        unique=True,
    )

    quotation_date = models.DateField()

    valid_until = models.DateField()

    sales_person = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="quotations",
    )

    status = models.CharField(
        max_length=20,
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

    class Meta:

        ordering = [
            "-quotation_date",
        ]

    def __str__(self):
        return self.quotation_number