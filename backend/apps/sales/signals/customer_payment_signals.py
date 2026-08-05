from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from apps.sales.models import CustomerPayment


@receiver(
    post_save,
    sender=CustomerPayment,
)
def customer_payment_saved(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Executes after a Customer Payment
    is created or updated.
    """

    if created:

        print(
            f"Customer Payment created: "
            f"{instance.payment_number}"
        )

    else:

        print(
            f"Customer Payment updated: "
            f"{instance.payment_number}"
        )