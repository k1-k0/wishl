from rest_framework import serializers
from .models import (
    Wish, Moneybox, Shop, Image, Tag
)


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish

class MoneyboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneybox


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
