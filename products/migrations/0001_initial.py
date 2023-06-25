# Generated by Django 4.2 on 2023-06-25 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('mainimage', models.ImageField(upload_to='products/productImg/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='category.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Productimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/productImg/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productimg', to='products.product', verbose_name='Product Name')),
            ],
        ),
        migrations.CreateModel(
            name='Productdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=255)),
                ('variant', models.CharField(max_length=255)),
                ('SKU', models.CharField(default=products.models.generate_sku, max_length=255, unique=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='productdetail', to='products.product', verbose_name='Product Name')),
            ],
        ),
    ]
