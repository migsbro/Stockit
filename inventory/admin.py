from django.contrib import admin
from .models import Item, ItemType

# Register your models here.
admin.site.register((Item, ItemType))