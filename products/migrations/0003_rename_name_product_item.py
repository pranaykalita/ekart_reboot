# Generated by Django 4.2.1 on 2023-05-12 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category_alter_product_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='item',
        ),
    ]
