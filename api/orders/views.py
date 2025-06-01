from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        expiration_time = timezone.now() + timedelta(hours=1)

        serializer.save(expiration_time=expiration_time)


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        order = self.get_object()

        if order.is_expired():
            order.status = 'expired'
            order.save()
        else:
            order.status = 'confirmed'
            order.save()

    def perform_destroy(self, instance):
        instance.cancel_order()


@api_view(['PUT'])
def confirm_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    if order.is_expired():
        return Response({"detail": "Order has expired."}, status=status.HTTP_400_BAD_REQUEST)

    order.confirm_order()
    return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def cancel_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    order.cancel_order()
    return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)

