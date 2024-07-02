from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Currency(models.Model):
    currency_abbr = models.CharField(max_length=3, unique=True)
    currency_symb = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.currency_abbr


class User(AbstractBaseUser):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    USERNAME_FIELD = "email"
