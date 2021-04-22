from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class ItemType(models.Model):
    name = models.CharField(max_length=45, null=False, unique=True)

    def __str__(self):
        return f"ID {self.id}: {self.name}"
    
    def get_absolute_url(self):
        return reverse("inventory:itemtype_list")

    class Meta:
        verbose_name_plural = "Item Types"


class Item(models.Model):
    name = models.CharField(max_length=45, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    description = models.CharField(max_length=45)
    quantity = models.IntegerField(null=False, default=0)
    itemtype = models.ForeignKey(ItemType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"ID {self.id}: {self.name} (${self.price})"

    def get_absolute_url(self):
        return reverse("inventory:item_detail", args=(self.id,))