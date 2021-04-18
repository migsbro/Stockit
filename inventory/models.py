from django.db import models
from django.conf import settings

# Create your models here.
class ItemType(models.Model):
    name = models.CharField(max_length=45, null=False)


class Item(models.Model):
    name = models.CharField(max_length=45, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    description = models.CharField(max_length=45)
    quantity = models.IntegerField(null=False, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    itemtype = models.ForeignKey(ItemType, null=True, on_delete=models.SET_NULL)