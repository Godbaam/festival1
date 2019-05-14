from django import forms
from .models import Lostfound ,Comment

class LostfoundPost(forms.ModelForm):
    image=forms.ImageField

    class Meta:
        model=Lostfound
        fields=['title', 'image','where','body']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('nickname','text')