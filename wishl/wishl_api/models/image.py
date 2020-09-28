from django.db import models


class Image(models.Model):
    url = models.URLField(blank=True)
