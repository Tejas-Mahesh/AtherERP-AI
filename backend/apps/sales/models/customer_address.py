from django.db import models

from apps.common.models import BaseModel

from .customer import Customer


class CustomerAddress(BaseModel):
    """
    Customer Address
    """

    ADDRESS_TYPES = [
        ("BILLING", "Billing"),
        ("SHIPPING", "Shipping"),
        ("OFFICE", "Office"),
        ("HOME", "Home"),
        ("OTHER", "Other"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="addresses",
    )

    address_type = models.CharField(
        max_length=20,
        choices=ADDRESS_TYPES,
        default="BILLING",
    )

    address_line_1 = models.CharField(
        max_length=255,
    )

    address_line_2 = models.CharField(
        max_length=255,
        blank=True,
    )

    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=20,
    )

    landmark = models.CharField(
        max_length=255,
        blank=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:

        ordering = [
            "address_type",
        ]

    def __str__(self):
        return (
            f"{self.customer.name} - {self.address_type}"
        )