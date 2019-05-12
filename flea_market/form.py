from django import forms
from .models import Flea_market

class Flea_marketPost(forms.ModelForm):
    image = forms.ImageField
   
    class Meta:
        model = Flea_market
        fields = ['title', 'image', 'body']