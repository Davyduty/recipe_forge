from django import forms
from recipeboxapp.models import Item, ImageModel


class Recipeform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'typ', 'description')


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']
