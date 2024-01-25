from django.db import models
from apps.product.models import Product
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Rating(models.Model):
    RATING_CHOICES = (
        (1,'Too bad'),
        (2,'bad'),
        (3,'Normal'),
        (4,'Good'),
        (5,'Perfect')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ['owner','product']
        


