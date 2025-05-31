from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta

# Serializer (defina os serializers para Order e OrderItem)



# Listar e Criar pedidos
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Definir o tempo de expiração, aqui setando 1 hora como exemplo
        expiration_time = timezone.now() + timedelta(hours=1)
        serializer.save(expiration_time=expiration_time)

    def get_queryset(self):
        # Filtro para retornar somente os pedidos do cliente logado
        return Order.objects.filter(customer=self.request.user)

# Detalhar, Confirmar e Cancelar Pedido
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        order = self.get_object()

        # Confirmar o pedido, se não expirou
        if order.is_expired():
            order.status = 'expired'
            order.save()
        else:
            order.status = 'confirmed'
            order.save()

    def perform_destroy(self, instance):
        instance.cancel_order()

# Confirmar pedido via PUT
@api_view(['PUT'])
def confirm_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    # Verificar se o pedido já expirou
    if order.is_expired():
        return Response({"detail": "Order has expired."}, status=status.HTTP_400_BAD_REQUEST)

    # Confirmar o pedido
    order.confirm_order()
    return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)

# Cancelar pedido via PUT
@api_view(['PUT'])
def cancel_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    # Cancelar o pedido
    order.cancel_order()
    return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)

