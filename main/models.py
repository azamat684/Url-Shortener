from django.db import models

# Create your models here.

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)