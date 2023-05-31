from django import forms
from django.forms import ModelForm

from catalog.models import Product, Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone', 'email', 'site')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'preview', 'is_published')



class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'category')
