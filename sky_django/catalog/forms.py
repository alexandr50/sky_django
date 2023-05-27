from django import forms
from django.forms import ModelForm

from catalog.models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=30)
    contact = forms.CharField(label='Номер телефона или email', max_length=30)


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'category')
