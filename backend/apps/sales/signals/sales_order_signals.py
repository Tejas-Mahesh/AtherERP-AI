from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from apps.sales.models import SalesOrder


@receiver(
    post_save,
    sender=SalesOrder,
)
def sales_order_saved(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Executes after a Sales Order
    is created or updated.
    """

    if created:

        print(
            f"Sales Order created: "
            f"{instance.sales_order_number}"
        )

    else:

        print(
            f"Sales Order updated: "
            f"{instance.sales_order_number}"
        )