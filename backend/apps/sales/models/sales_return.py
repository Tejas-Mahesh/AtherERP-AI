from django.db import models

from apps.common.models import BaseModel
from apps.accounts.models import User

from .customer import Customer
from .sales_invoice import SalesInvoice


class SalesReturn(BaseModel):
    """
    Customer Sales Return
    """

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("RECEIVED", "Received"),
        ("APPROVED", "Approved"),
        ("REFUNDED", "Refunded"),
        ("REJECTED", "Rejected"),
    ]

    RETURN_REASONS = [
        ("DAMAGED", "Damaged"),
        ("DEFECTIVE", "Defective"),
        ("WRONG_ITEM", "Wrong Item"),
        ("EXPIRED", "Expired"),
        ("CUSTOMER_REQUEST", "Customer Request"),
        ("OTHER", "Other"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="sales_returns",
    )

    sales_invoice = models.ForeignKey(
        SalesInvoice,
        on_delete=models.PROTECT,
        related_name="sales_returns",
    )

    return_number = models.CharField(
        max_length=30,
        unique=True,
    )

    return_date = models.DateField()

    reason = models.CharField(
        max_length=30,
        choices=RETURN_REASONS,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_sales_returns",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = [
            "-return_date",
        ]

    def __str__(self):
        return self.return_number