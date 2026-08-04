from django.db import models

from apps.common.models import BaseModel
from apps.accounts.models import User
from apps.inventory.models import Warehouse

from .sales_order import SalesOrder


class DeliveryNote(BaseModel):
    """
    Delivery Note
    """

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("DISPATCHED", "Dispatched"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]

    sales_order = models.ForeignKey(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name="delivery_notes",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="delivery_notes",
    )

    delivery_number = models.CharField(
        max_length=30,
        unique=True,
    )

    delivery_date = models.DateField()

    delivered_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="delivery_notes",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    vehicle_number = models.CharField(
        max_length=30,
        blank=True,
    )

    transporter_name = models.CharField(
        max_length=150,
        blank=True,
    )

    tracking_number = models.CharField(
        max_length=100,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = [
            "-delivery_date",
        ]

    def __str__(self):
        return self.delivery_number