from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from apps.sales.models import DeliveryNote


@receiver(
    post_save,
    sender=DeliveryNote,
)
def delivery_note_saved(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Executes after a Delivery Note
    is created or updated.
    """

    if created:

        print(
            f"Delivery Note created: "
            f"{instance.delivery_number}"
        )

    else:

        print(
            f"Delivery Note updated: "
            f"{instance.delivery_number}"
        )