from django.db import models
from django.contrib.auth.models import User

from .moneybox import Moneybox
from .shop import Shop
from .tag import Tag
from .image import Image


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    money = models.ForeignKey(Moneybox, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

