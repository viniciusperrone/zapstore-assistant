from django.db import models

from products.models import Product


class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sales')

    quantity = models.IntegerField(default=1)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
