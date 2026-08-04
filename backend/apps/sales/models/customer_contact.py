from django.db import models

from apps.common.models import BaseModel

from .customer import Customer


class CustomerContact(BaseModel):
    """
    Customer Contact Person
    """

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="contacts",
    )

    name = models.CharField(
        max_length=150,
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    department = models.CharField(
        max_length=100,
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
        blank=True,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = [
            "name",
        ]

    def __str__(self):
        return (
            f"{self.customer.name} - {self.name}"
        )