from django.db import models

from .managers import SiteManager


class Site(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SiteManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SiteEntry(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    value_a = models.DecimalField(max_digits=5, decimal_places=2)
    value_b = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['created_at']
