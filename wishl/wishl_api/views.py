from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status

from .serializers import (
    UserSerializer, WishSerializer, MoneyboxSerializer, ShopSerializer, ImageSerializer, TagSerializer
)

from .models import Wish, Tag, Image, Moneybox, Shop


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class WishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wishes to be viewed or edited.
    """
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoneyboxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows moneyboxes to be viewed or edited.
    """
    queryset = Moneybox.objects.all()
    serializer_class = MoneyboxSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shops to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

