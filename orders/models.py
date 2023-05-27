import uuid

from account.models import *


# Create your models here.

def generate_orderid():
    uuid_string = str(uuid.uuid4()).replace('-', '')[:8]
    sku = 'ORDER-' + uuid_string.upper()
    return sku


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    items = models.JSONField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    orderno = models.CharField(max_length=255, default=generate_orderid, unique=True)
    orderstatus = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    payment = models.CharField(max_length=50, default="cash")

    def __str__(self):
        return f"Order {self.id}"


class Orderaddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderaddress')

    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal = models.CharField(max_length=20)

    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.order}, {self.city}, {self.state}, {self.country}"


class orderapprovals(models.Model):
    Approval_status = [
        ('pending', 'pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='sellerstatus')
    seller = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='selleraccount')
    approval = models.CharField(max_length=50, choices=Approval_status, default='pending')
    note = models.TextField()

    def __str__(self):
        return f"{self.order}, {self.seller}, {self.note}"
