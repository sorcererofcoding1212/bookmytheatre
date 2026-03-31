from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AccountManager

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Account(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email
