from rest_framework import serializers
from .models import Category, Currency, Finances, Goals, Users


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('__all__')


class FinancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finances
        fields = ('__all__')


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ('__all__')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'lastname', 'login')
