from django.db import models
from apps.product.models import Product
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.title

class Order(models.Model):

    STATUS_ORDER = (
        ('in_process', 'В процессе'),
        ('completed', 'Завершино')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through=OrderItem)
    address = models.CharField(max_length=90)
    number = models.CharField(max_length=60)
    status = models.CharField(choices=STATUS_ORDER, max_length=20, default='in process')
    total_sum = models.PositiveIntegerField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.id} -----> {self.user}'




