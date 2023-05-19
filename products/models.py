import uuid

from account.models import *
from category.models import *
from .imageResize import resize_image


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', default=None)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategory')
    mainimage = models.ImageField(upload_to='products/productImg/')
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='seller')

    # resize image to perfect fit
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        img = resize_image(self.mainimage.path)
        img.save(self.mainimage.path)

    def __str__(self):
        return self.name


def generate_sku():
    uuid_string = str(uuid.uuid4()).replace('-', '')[:8]
    sku = 'SKU-' + uuid_string.upper()
    return sku


class Productdetails(models.Model):
    product = models.OneToOneField(Product, verbose_name="Product Name", on_delete=models.CASCADE, related_name='productdetail')
    about = models.TextField()
    description = models.TextField()
    size = models.CharField(max_length=255)
    variant = models.CharField(max_length=255)
    SKU = models.CharField(max_length=255, default=generate_sku, unique=True)

    def __str__(self):
        return f"{self.product.name} details"


class Productimage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product Name", related_name='productimg')
    image = models.ImageField(upload_to='products/productImg/')

    # resize image to perfect fit
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        img = resize_image(self.image.path)
        img.save(self.image.path)

    def __str__(self):
        return f"{self.product.name} image"
