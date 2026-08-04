from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Organization
from apps.accounts.models import User

from .customer import Customer
from .quotation import Quotation


class SalesOrder(BaseModel):
    """
    Sales Order
    """

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("CONFIRMED", "Confirmed"),
        ("PROCESSING", "Processing"),
        ("PARTIALLY_DELIVERED", "Partially Delivered"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="sales_orders",
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="sales_orders",
    )

    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_orders",
    )

    sales_order_number = models.CharField(
        max_length=30,
        unique=True,
    )

    order_date = models.DateField()

    expected_delivery_date = models.DateField(
        null=True,
        blank=True,
    )

    sales_person = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_orders",
    )

    status = models.CharField(
        max_length=30,
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
        related_name="approved_sales_orders",
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
        return self.sales_order_number