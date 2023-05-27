# Generated by Django 4.2.1 on 2023-05-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_orderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderapprovals',
            name='approval',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('delivered', 'Delivered')], default='pending', max_length=50),
        ),
    ]
