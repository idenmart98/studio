from django import forms
from .models import ShopListItem

class ShopListItemForm(forms.ModelForm):
    class Meta:
        model = ShopListItem
        fields = ['name', 'price']
