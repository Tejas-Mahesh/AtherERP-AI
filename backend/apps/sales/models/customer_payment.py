from django.db import models

from apps.common.models import BaseModel
from apps.accounts.models import User

from .customer import Customer
from .sales_invoice import SalesInvoice


class CustomerPayment(BaseModel):
    """
    Customer Payment
    """

    PAYMENT_METHODS = [
        ("CASH", "Cash"),
        ("BANK_TRANSFER", "Bank Transfer"),
        ("CHEQUE", "Cheque"),
        ("UPI", "UPI"),
        ("CARD", "Card"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
        ("CANCELLED", "Cancelled"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    sales_invoice = models.ForeignKey(
        SalesInvoice,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    payment_number = models.CharField(
        max_length=30,
        unique=True,
    )

    payment_date = models.DateField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True,
    )

    received_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="received_customer_payments",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="COMPLETED",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = [
            "-payment_date",
        ]

    def __str__(self):
        return self.payment_number