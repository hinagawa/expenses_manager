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


class Category(models.Model):
    category = models.CharField(max_length=30, unique=True)
    is_custom = models.BooleanField()
    user_id = models.ForeignKey(Users,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    def __str__(self):
        return self.category


class Goals(models.Model):
    name = models.CharField(max_length=256)
    target_sum = models.IntegerField()
    current_sum = models.IntegerField()
    deadline = models.DateField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)


class Finances(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_expenses = models.BooleanField
    user_id = models.ForeignKey(Users,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

