from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    Wish, Moneybox, Shop, Image, Tag
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'username', 'email'
        ]

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['user', 'title', 'money']


class MoneyboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneybox
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
