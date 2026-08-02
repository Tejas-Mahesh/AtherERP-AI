from django.db import models
from apps.common.models import BaseModel
from apps.organizations.models import Organization


class Supplier(BaseModel):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="suppliers",
    )

    name = models.CharField(max_length=200)

    email = models.EmailField(blank=True)

    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name