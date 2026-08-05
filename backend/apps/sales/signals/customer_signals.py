from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.sales.models import Customer


@receiver(post_save, sender=Customer)
def customer_created(
    sender,
    instance,
    created,
    **kwargs,
):
    """
    Execute after a customer is created.
    """

    if created:
        print(
            f"Customer created: {instance.customer_code}"
        )