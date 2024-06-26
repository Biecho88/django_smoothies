from django.db import models


class Categories(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Smoothie(models.Model):
    category = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    ingredients = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    nutrition = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name