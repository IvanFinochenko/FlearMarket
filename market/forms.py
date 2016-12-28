from django.forms import ModelForm

from market.models import Item


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category']