from django import forms
from .models import Choices


class ShortcutForm(forms.ModelForm):

    class Meta:
        model = Choices
        exclude = ['name']
