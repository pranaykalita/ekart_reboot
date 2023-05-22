from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models


# Create your models here.

class CustomerUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Create normal User
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_seller', False)
        return self._create_user(email, password, **extra_fields)

    # Create SuperUser
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_seller', True)
        return self._create_user(email, password, **extra_fields)

    # create Seller
    def create_seller(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_seller', True)
        return self._create_user(email, password, **extra_fields)

    # Create Customer
    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_seller', False)
        extra_fields.setdefault('is_customer', True)
        return self._create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class CustomerUser(AbstractUser, PermissionsMixin):

    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255,default=None,null=True)
    lastname = models.CharField(max_length=255,default=None,null=True)

    # default Create Customer
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_accounts',
        related_query_name='user_account',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_accounts',
        related_query_name='user_account',
    )

    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'CustomerUser'
        verbose_name_plural = 'CustomerUsers'


class Customerdetail(models.Model):
    customeruser = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, related_name='customer', verbose_name='Profile')
    mobile = models.CharField(max_length=12)
    profileimg = models.ImageField(upload_to='profile/profileimg')

    def __str__(self):
        return self.customeruser.email
