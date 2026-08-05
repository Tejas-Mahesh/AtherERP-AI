from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from apps.sales.models import SalesReturn


@receiver(
    post_save,
    sender=SalesReturn,
)
def sales_return_saved(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Executes after a Sales Return
    is created or updated.
    """

    if created:

        print(
            f"Sales Return created: "
            f"{instance.return_number}"
        )

    else:

        print(
            f"Sales Return updated: "
            f"{instance.return_number}"
        )