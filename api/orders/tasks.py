from celery import shared_task
from django.utils import timezone

from orders.models import Order


@shared_task
def expire_order(order_id):
    try:
        order = Order.objects.get(id=order_id)

        if order.status == 'pending':
            order.status = 'expired'
            order.updated_at = timezone.now()
            order.save()
    except Exception as err:
        print(str(err))
