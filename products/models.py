from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("products:dynamic", kwargs={"my_id":self.id})  # f"/dynamic/{ self.id }/"