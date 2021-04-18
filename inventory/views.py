from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.
class InventoryList(ListView):
    template_name = "item/list.html"
    model = Item
    context_object_name = "items"


class InventoryDetail(DetailView):
    template_name = "item/detail.html"
    model = Item
    context_object_name = "item"