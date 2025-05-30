from django.db import models
from django.utils import timezone
from products.models import Product
from customers.models import Customer


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('expired', 'Expired'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderItem')
    expiration_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_expired(self):
        """Verifica se o pedido expirou"""
        return timezone.now() > self.expiration_time

    def confirm_order(self):
        """Confirma o pedido e altera o status"""
        if not self.is_expired():
            self.status = 'confirmed'
            self.save()
            self.update_product_quantities()
        else:
            self.status = 'expired'
            self.save()

    def cancel_order(self):
        """Cancela o pedido e volta a quantidade do produto"""
        self.status = 'canceled'
        self.save()
        self.restore_product_quantities()

    def update_product_quantities(self):
        """Atualiza a quantidade de produtos reservados no estoque"""
        for item in self.order_items.all():
            item.product.quantity -= item.quantity
            item.product.save()

    def restore_product_quantities(self):
        """Restaura a quantidade de produtos em estoque"""
        for item in self.order_items.all():
            item.product.quantity += item.quantity
            item.product.save()

    def __str__(self):
        return f'Order #{self.id} - {self.customer.name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'
