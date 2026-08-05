from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from apps.sales.models import Quotation


@receiver(
    post_save,
    sender=Quotation,
)
def quotation_saved(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Executes after a quotation is created
    or updated.
    """

    if created:

        print(
            f"Quotation created: "
            f"{instance.quotation_number}"
        )

    else:

        print(
            f"Quotation updated: "
            f"{instance.quotation_number}"
        )