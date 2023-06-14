from django import forms
from django.forms import ModelForm

from catalog.models import Product, Contact, Post, Version

INCORRECT_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ContactForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone', 'email', 'site')

class PostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'preview', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['is_published'].widget.attrs['class'] = 'form-choice'



class CreateProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'category')

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title').lower()
        if cleaned_data in INCORRECT_WORDS:
            raise forms.ValidationError('Недопустимое название')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').lower()
        for item in INCORRECT_WORDS:
            if item in cleaned_data:
                raise forms.ValidationError('Недопустимое слово в описании')
        return cleaned_data


class UpdateProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'category')




class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name_version', 'number_version', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['is_active'].widget.attrs['class'] = 'form-choice'