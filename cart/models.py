import uuid

from django.db import models

from account.models import CustomerUser
from products.models import Product


# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    customer = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, related_name='cartcustomer', )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartproduct')
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.product:
            self.total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.cart)
