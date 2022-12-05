from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']

    # name = forms.CharField()
    # geeks_field = forms.ImageField()
