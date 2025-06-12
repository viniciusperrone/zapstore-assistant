from celery import shared_task
from django.utils import timezone

from orders.models import Order


@shared_task
def expire_pending_orders():
    now = timezone.now()

    expired_orders = Order.objects.filter(status='pending', expiration_time__lt=now)

    for order in expired_orders:
        order.status = 'expired'
        order.save()
