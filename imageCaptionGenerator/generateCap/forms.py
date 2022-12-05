from django import forms

class ImageForm(forms.Form):
    name = forms.CharField()
    geeks_field = forms.ImageField()
