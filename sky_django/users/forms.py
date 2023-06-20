from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'






class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        # self.fields['avatar'].widget.attrs['class'] = 'costom-file-input'

