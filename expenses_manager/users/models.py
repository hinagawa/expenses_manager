from django.db import models


class Currency(models.Model):
    currency_abbr = models.CharField(max_length=3, unique=True)
    currency_symb = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.currency_abbr


class Users(models.Model):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
