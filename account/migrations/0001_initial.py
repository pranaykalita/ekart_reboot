# Generated by Django 4.2 on 2023-06-25 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(default=None, max_length=255, null=True)),
                ('lastname', models.CharField(default=None, max_length=255, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_accounts', related_query_name='user_account', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_accounts', related_query_name='user_account', to='auth.permission')),
            ],
            options={
                'verbose_name': 'CustomerUser',
                'verbose_name_plural': 'CustomerUsers',
            },
        ),
        migrations.CreateModel(
            name='Customerdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=12)),
                ('profileimg', models.ImageField(upload_to='profile/profileimg')),
                ('customeruser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Profile')),
            ],
        ),
    ]
