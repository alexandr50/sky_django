from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=30)
    contact = forms.CharField(label='Номер телефона или email', max_length=30)
