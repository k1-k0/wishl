from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
