"""Models."""
from django.db import models


# Create your models here.
class Tweet(models.Model):
    """Model Tweet."""

    tweet = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
