from django.db import models
from django.core.exceptions import ValidationError


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=125, unique=True)
    tax_document = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=555)
    state = models.CharField(max_length=555)
    zip_code = models.CharField(max_length=8)

    def save(self, *args, **kwargs):
        if len(self.tax_document) < 11 or len(self.zip_code) < 8:
            raise ValidationError('The tax document/zip_code fields do not respect the minimum character length')

        return super().save(*args, **kwargs)
