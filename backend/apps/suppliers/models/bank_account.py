from django.db import models

from apps.common.models import BaseModel
from .supplier import Supplier


class SupplierBankAccount(BaseModel):
    """
    Bank account details of a supplier.
    """

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="bank_accounts",
    )

    bank_name = models.CharField(
        max_length=200,
    )

    branch_name = models.CharField(
        max_length=200,
        blank=True,
    )

    account_holder_name = models.CharField(
        max_length=200,
    )

    account_number = models.CharField(
        max_length=50,
    )

    ifsc_code = models.CharField(
        max_length=20,
        blank=True,
    )

    swift_code = models.CharField(
        max_length=20,
        blank=True,
    )

    account_type = models.CharField(
        max_length=50,
        default="Current",
    )

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["bank_name"]
        verbose_name = "Supplier Bank Account"
        verbose_name_plural = "Supplier Bank Accounts"

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"