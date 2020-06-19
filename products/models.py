from django.db import models
from datetime import datetime
from salesmanager.models import Salesmanager


class Product(models.Model):
    salesmanager = models.ForeignKey(Salesmanager, on_delete=models.DO_NOTHING)
    productname = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/%Y/%M/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.productname
