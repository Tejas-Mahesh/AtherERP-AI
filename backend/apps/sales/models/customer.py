from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization
from apps.accounts.models import User


class Customer(BaseModel):
    """
    Customer Master
    """

    CUSTOMER_TYPES = [
        ("INDIVIDUAL", "Individual"),
        ("BUSINESS", "Business"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("BLOCKED", "Blocked"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="customers",
    )

    customer_code = models.CharField(
        max_length=30,
    )

    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPES,
        default="BUSINESS",
    )

    name = models.CharField(
        max_length=200,
    )

    company_name = models.CharField(
        max_length=200,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    mobile_number = models.CharField(
        max_length=20,
    )

    gst_number = models.CharField(
        max_length=30,
        blank=True,
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
    )

    credit_limit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    payment_terms = models.PositiveIntegerField(
        default=30,
        help_text="Credit days",
    )

    sales_person = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_customers",
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

        ordering = [
            "name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "customer_code",
                ],
                name="unique_customer_code_per_organization",
            ),
        ]

    def __str__(self):
        return f"{self.customer_code} - {self.name}"