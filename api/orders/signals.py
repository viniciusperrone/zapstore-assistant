from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from orders.tasks import expire_order


EXPIRATION_TIME = 120

@receiver(post_save, sender=Order)
def schedule_order_expiration(sender, instance, created, **kwargs):
    if created:
        expire_order.apply_async(args=[instance.id], countdown=EXPIRATION_TIME)
