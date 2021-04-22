from django import forms
from .models import Item, ItemType

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"