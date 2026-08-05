from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from apps.sales.models import SalesInvoice


@receiver(
    post_save,
    sender=SalesInvoice,
)
def sales_invoice_saved(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Executes after a Sales Invoice
    is created or updated.
    """

    if created:

        print(
            f"Sales Invoice created: "
            f"{instance.invoice_number}"
        )

    else:

        print(
            f"Sales Invoice updated: "
            f"{instance.invoice_number}"
        )