from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    active = models.BooleanField(default=True)
    objects = models.Manager()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"my_id":self.id})