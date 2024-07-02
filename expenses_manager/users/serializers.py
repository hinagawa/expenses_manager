from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Currency

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "lastname", "email", "password", "currency")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)  # This hashes and salts the password
        user.save()
        return user


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"
