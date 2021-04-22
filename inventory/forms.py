from django import forms
from .models import Item, ItemType

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


class ItemTypeForm(forms.ModelForm):
    class Meta:
        model = ItemType
        fields = "__all__"