from django import forms
from django.forms import ModelForm
from .models import *


class appForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = App
        fields = '__all__'
