from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Item, ItemType
from .forms import ItemForm, ItemTypeForm

# Create your views here.
class ItemList(ListView):
    template_name = "items/list.html"
    model = Item
    context_object_name = "items"


class ItemDetail(DetailView):
    template_name = "items/detail.html"
    model = Item
    context_object_name = "item"


class ItemCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "items/new_or_update.html"
    model = Item
    form_class = ItemForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "items/new_or_update.html"
    model = Item
    form_class = ItemForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "items/delete.html"
    model = Item
    success_url = reverse_lazy("inventory:item_list")

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemTypeList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "itemtypes/list.html"
    model = ItemType
    context_object_name = "itemtypes"

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemTypeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "itemtypes/new_or_update.html"
    model = ItemType
    form_class = ItemTypeForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemTypeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "itemtypes/new_or_update.html"
    model = ItemType
    form_class = ItemTypeForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemTypeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "itemtypes/delete.html"
    model = ItemType
    success_url = reverse_lazy("inventory:itemtype_list")

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff