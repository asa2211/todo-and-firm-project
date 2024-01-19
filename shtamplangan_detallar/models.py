from django.db import models
from todo.models import CustomUser

class ProductModel(models.Model):
    product_name = models.CharField(max_length=150)
    description = models.TextField(default='')
    added_at = models.DateTimeField(auto_created=True, null=True, blank=False)

    def __str__(self):
        return self.product_name


class OrderModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    index = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_created=True, null=True, blank=False)


class GaleryModel(models.Model):
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, related_name='p')
    image = models.ImageField(upload_to='photo', null=True, blank=False)


class OrderStatusModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    CHOICES = (
        (1, 'confirmed'),
        (2, 'processing'),
        (3, "fineshed")
    )
    status = models.PositiveSmallIntegerField(default=1, choices=CHOICES)
