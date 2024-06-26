from django.db import models
from users.models import User


class Category(models.Model):
    category = models.CharField(max_length=30, unique=True)
    is_custom = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category


class Goal(models.Model):
    name = models.CharField(max_length=256)
    target_sum = models.IntegerField()
    current_sum = models.IntegerField()
    deadline = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Finance(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateField(auto_now_add=True)
    is_expenses = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
