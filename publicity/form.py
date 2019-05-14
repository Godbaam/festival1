from django import forms
from .models import Publicity

class Publicity_Post(forms.ModelForm):
    class Meta:
        model = Publicity
        fields = ['title', 'image', 'body']