from rest_framework import serializers
from .models import Category, Finances, Goals


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FinancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finances
        fields = "__all__"


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = "__all__"
